










"""
This is a cookiecutter example of a simple example beam job.

This job finds the most streamed track per country from Streams and joins in track_name
from a bigquery table. The purpose of this is to show examples of reading/writing to BQ
and GCS and various ways of processing in Beam.
"""
import datetime
import logging
from argparse import ArgumentParser
import apache_beam as beam
from apache_beam.io import ReadFromBigQuery, WriteToAvro, WriteToBigQuery
from apache_beam.options.pipeline_options import PipelineOptions


ALLOWED_LANGUAGES = ("en-us",)
logger = logging.getLogger("OAI Subscript Pipeline")

### read/define schema
from pathlib import Path
from fastavro.schema import load_schema

AVRO_PATH = Path(__file__).parent

AVRO_OPEN_AI_SCORER_SCHEMA = load_schema(AVRO_PATH / "oai.avsc")

BQ_OPEN_AI_SCORER_SCHEMA = {
    "fields": [
        dict(name="episode_uri", type="STRING", mode="REQUIRED"),
        dict(
            name="subscripts",
            type="RECORD",
            mode="REPEATED",
            fields=[
                dict(name="subscript_id", type="STRING", mode="REQUIRED"),
                dict(name="hate", type="FLOAT", mode="NULLABLE"),
                dict(name="hate_threatening", type="FLOAT", mode="NULLABLE"),
                dict(name="self_harm", type="FLOAT", mode="NULLABLE"),
                dict(name="sexual", type="FLOAT", mode="NULLABLE"),
                dict(name="sexual_minors", type="FLOAT", mode="NULLABLE"),
                dict(name="violence", type="FLOAT", mode="NULLABLE"),
                dict(name="violence_graphic", type="FLOAT", mode="NULLABLE"),
            ],
        ),
    ]
}
### end schema


class OpenAiJobOptions(PipelineOptions):
    @classmethod
    def _add_argparse_args(cls, parser: ArgumentParser) -> None:
        # Add any job specific args here
        parser.add_argument("--subscript-input-today", required=True)
        parser.add_argument("--subscript-input-yesterday", required=True)
        parser.add_argument("--output-bq", required=True)
        parser.add_argument("--output-gcs", required=True)


def open_ai_pipeline(options: OpenAiJobOptions) -> None:
    """Build and run the pipeline.
    Separated from main for the purpose of testing.
    """
    with beam.Pipeline(options=options) as p:
        spodnik_subscripts = p | "subscripts" >> ReadFromBigQuery(
            query=f"""
            SELECT uri as subscript_uri, text
            FROM `{options.subscript_input_today.replace(":", ".")}`
            WHERE language in {ALLOWED_LANGUAGES}
            EXCEPT DISTINCT
            SELECT uri as subscript_uri, text
            FROM `{options.subscript_input_yesterday.replace(":", ".")}`
            WHERE language in {ALLOWED_LANGUAGES}
            """,
            # today's uris minus yesterday's = only new ones added today (dataset is cumulative daily)
            use_standard_sql=True,
        )

        class OpenAiCallFn(beam.DoFn):
            def process(self, e):
                pass

        scored_responses = spodnik_subscripts | "Send requests to OAI" >> beam.ParDo(OpenAiCallFn(False))

        # -> [(episode_uri, snippet), ...]

        class compose_bq_output(beam.DoFn):
            def process(self, e):
                output_pcoll = {}
                output_pcoll["episode_uri"] = e[0]
                output_pcoll["subscripts"] = e[1]
                logger.log(level=logging.INFO, msg=output_pcoll)
                yield output_pcoll

        joined_subscripts_with_descr_score = (
                scored_responses
                | "Group subscripts by episode_uri" >> beam.GroupByKey()  # [(unique_episode_uri, list_of_subscripts), ...]
                | "Compose to output format" >> beam.ParDo(compose_bq_output())
        )
        # {"episode_uri": abc123xyz, "subscripts":[(...)]}

        # Write to Bigquery
        joined_subscripts_with_descr_score | "Write to BQ" >> WriteToBigQuery(
            table=options.output_bq,
            schema=BQ_OPEN_AI_SCORER_SCHEMA,
            write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE,
            create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
            additional_bq_parameters={
                "destinationTableProperties": {
                    "description": "{ policy: { accessTier: BROAD },"
                                   " description: 'subscripts scored via openAI' }"
                },
            },
        )

        # Write to GCS
        joined_subscripts_with_descr_score | "Write to GCS" >> WriteToAvro(
            f"{options.output_gcs}/part",
            AVRO_OPEN_AI_SCORER_SCHEMA,
            file_name_suffix=".avro",
        )


def main() -> None:
    logging.getLogger().setLevel(logging.INFO)

    # Parse command-line args, both job specific and all Beam PipelineOptions
    opts = OpenAiJobOptions()

    open_ai_pipeline(opts)


if __name__ == "__main__":
    main()





