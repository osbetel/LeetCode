"""
spark rdd vs df apis:
- rdd: resilient distributed dataset, used for unstructured data, low level control, want to execute operations with 
       functional programming vs domain specific expressions. would be used for text streams or media streams like audio.
       data is not organized into named columns. collection of data objects across nodes in spark cluster
- dataframe: data is organized into columns, we can consider this to be like a table that we can execute SQL-like ops on like
             joins, group bys, etc. It imposes a structure onto the data.
- dataset (new): can consider dataframe as dataset[Row] where [Row] is an ambiguous type. Vs dataset which is more dataset[T] for a 
                 strongly typed dataframe. Only exists in java/scala due to Python lacking type safety at compile time

lets practice using spark to take a sequence of youtube URLs, generate uuids, pull the audio file, and then turn it into a vector embedding
"""

# from pyspark.sql import SparkSession

# # first create spark session
# spark = (
#     SparkSession.builder
#     .appName("audio_processing")
#     .getOrCreate()
# )

# # now need to get source data, should be (key, url)
# data = [
#     (1, "https://www.youtube.com/watch?v=NAP-KRCyLv4"),   # martin garrix sleepless night
#     (2, "https://www.youtube.com/watch?v=Gjxm1s26dXY"),   # martin garrix carry you
#     (3, "https://www.youtube.com/watch?v=zw47ymC0RNQ"),   # saib in your arms
#     (4, "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),   # rick roll
#     (5, "https://www.youtube.com/watch?v=kJQP7kiw5Fk"),   # despacito
#     (6, "https://www.youtube.com/watch?v=9bZkp7q19f0"),   # gangnam style
#     (7, "https://www.youtube.com/watch?v=YQHsXMglC9A"),   # hello adele
#     (8, "https://www.youtube.com/watch?v=hT_nvWreIhg"),   # counting stars
# ]

# columns = ["song_id", "url"]

# df = spark.createDataFrame(data, columns)
# df.show()

"""
# -- Content dimension (global content attributes only)
dim_content = [
    content_key: int (surrogate key),
    content_id: str (natural key),
    title: str,
    content_category: str,
    production_type: str,
    production_cost_usd: float,
    production_country: str,
    release_date: date
]

# -- Region dimension  
dim_region = [
    region_key: int,
    region: str
]

# -- Date dimension
dim_date = [
    date_key: int,
    date: date,
    year: int,
    month: int,
    quarter: int,
    day_of_week: str
]

# -- Fact table for performance metrics
fact_performance = [
    content_key: int (FK),
    region_key: int (FK), 
    date_key: int (FK),
    total_hours_watched: int,
    unique_viewers: int,
    avg_completion_rate: float
]

# -- Fact table for content availability (captures licensing events)
fact_content_availability = [
    content_key: int (FK),
    region_key: int (FK),
    availability_date_key: int (FK),
    licensing_cost_usd: float
]
"""

"""
Write a SQL query that answers: "What is the ROI (return on investment) for 
each content category in the last 6 months, calculated as total hours watched 
per dollar invested, and rank them from best to worst ROI?"

with last_six_months_performance as (
    select content_key, region_key, total_hours_watched
    from dim_date dt
    join fact_performance p
    on dt.date_key = p.date_key
    where dt.date between current_date() - interval 6 month and current_date()
), -- all rows from performance table in the last 6 months

content_avail_last_six_months as (
    select content_key, region_key, licensing_cost_usd
    from dim_date dt
    join fact_content_availability ca
    on dt.date_key = ca.date_key
    where dt.date between current_date() - interval 6 month and current_date()
)

regional_metrics as (
    select lsmp.content_key, sum(total_hours_watched) sum_hours, sum(licensing_cost_usd) as sum_license_cost
    from last_six_months_performance lsmp
    join content_avail_last_six_months calsm
    on lsmp.content_key = calsm.content_key and lsmp.region_key = calsm.region_key
    group by lsmp.content_key
) -- have rows like (content_key, sum_hours, sum_license_cost) for each content and region key

ROI as (
    select content_category, (sum(sum_hours) / (sum(production_cost_usd) + sum(sum_license_cost))) as roi
    from dim_content c
    join regional_metrics rm
    on c.content_key = rm.content_key
    group by content_category
    order by roi desc
) -- at this point we have content_category, roi, eg: horror, 120.2 hrs per $1 spent)
"""


from pyspark.sql import SparkSession

data = [
    "s3://netflix-raw/production_data/",
    "s3://netflix-raw/performance_metrics/",
    "s3://netflix-raw/regional_availability/",
]

prod_data = [
    ("content_id", "title", "production_type", "production_cost_usd", "production_country", "release_date", "content_category"),
    ("series_123", "Mystery Drama", "original", 45000000, "US", "2024-03-15", "series"),
    ("movie_456", "Action Thriller", "licensed", 8000000, "UK", "2024-05-20", "movie"),
    ("series_789", "Comedy Special", "original", 2000000, "CA", "2024-07-10", "special"),
]

perf_metrics = [
    ("content_id", "metric_date", "total_hours_watched", "unique_viewers", "avg_completion_rate", "region"),
    ("series_123", "2024-04-01", 2500000, 180000, 0.78, "US"),
    ("series_123", "2024-04-01", 1200000, 95000, 0.72, "EU"),
    ("movie_456", "2024-06-01", 800000, 120000, 0.85, "US"),
]

reg_avail = [
    ("content_id", "region", "availability_start_date", "licensing_cost_usd"),
    ("series_123", "US", "2024-03-15", 0),
    ("series_123", "EU", "2024-03-20", 500000),
    ("movie_456", "US", "2024-05-20", 8000000),
]

spark = (
    SparkSession.builder
    .appName("roi calculation")
    .getOrCreate()
)

def read_sample_data(d):
    cols = d[0]
    data = d[1:]
    return spark.createDataFrame(data, cols)

data_sets = [prod_data, perf_metrics, reg_avail]
dfs = [read_sample_data(x) for x in data_sets]

df_prod, df_perf, df_reg = dfs

# create dimensional models
from pyspark.sql.functions import row_number, col, to_date, sum as spark_sum
from pyspark.sql import Window

dim_content = (
    df_prod.withColumn(
        "content_key",
        row_number().over(Window.orderBy("content_id"))
    )
)
# dim_content.show()

dim_region = (
    df_reg
    .select(col("region"))
    .distinct()
    .withColumn(
        "region_key",
        row_number().over(Window.orderBy("region"))
    )
)
# dim_region.show()

dim_date = (
    df_perf
    .withColumnRenamed("metric_date", "dt_str")
    .select("dt_str")
    .unionAll(
        df_reg
        .withColumnRenamed("availability_start_date", "dt_str")
        .select("dt_str")
    )
    .distinct()
    .withColumn("date_key", row_number().over(Window.orderBy("dt_str")))
    .withColumn("dt", to_date(col("dt_str"), "yyyy-MM-dd"))
    .drop(col("dt_str"))
)
# dim_date.show()

fact_performance = (
    df_perf
    .join(
        dim_content,
        "content_id"
    )
    .join(
        dim_region,
        "region"
    )
    .join(
        dim_date,
        df_perf["metric_date"] == dim_date["dt"]
    )
    .select(
        "content_key",
        "region_key",
        "date_key",
        "total_hours_watched",
        "unique_viewers",
        "avg_completion_rate",
        "production_cost_usd",
    )
)
# fact_performance.show()

fact_content_availability = (
    dim_content
    .join(
        df_reg,
        "content_id"
    )
    .join(
        dim_region,
        "region"
    )
    .select(
        "content_key",
        "region_key",
        "content_category",
        "availability_start_date",
        "licensing_cost_usd",
    )
)
# fact_content_availability.show()

# now to the actual ROI calculation

roi = (
    dim_date
    .join(
        fact_performance,
        "date_key"
    )
    .select(
        "content_key",
        "region_key",
        "date_key",
        "total_hours_watched",
        "production_cost_usd",
    )
    .join(
        fact_content_availability,
        "content_key"
    )
    .drop(
        fact_content_availability["region_key"],
        "availability_start_date"
    )
    .groupBy("content_category")
    .agg(
        spark_sum("licensing_cost_usd").alias("total_licensing_cost"),
        spark_sum("production_cost_usd").alias("total_prod_cost_usd"),
        spark_sum("total_hours_watched").alias("hrs_watched"),
    )
    .select(
        "content_category",
        (col("hrs_watched") / (col("total_licensing_cost") + col("total_prod_cost_usd"))).alias("roi")
    )
)
roi.show()

# how to make and apply a udf
from pyspark.sql.functions import udf
from pyspark.sql.types import FloatType
def roi_to_str(s):
    return str(s)

to_str_udf = udf(roi_to_str, FloatType())
df_w_str_roi = roi.withColumn("roi_str", to_str_udf(roi["roi"]))




"""
-- do total watch time
with views as (
    select content_id, sum(watch_duration_minutes) as total_viewed_minutes
    from user_views
    where view_date between current_date() - interval 30 days and current_date()
    group by content_id
) -- sum of all watched minutes in last 30 days by content_id

select v.content_id, title, total_viewed_minutes
from views v
join content c
on v.content_id = c.content_id
where content_type = 'movie'
order by total_viewed_minutes desc
limit 5
"""

"""
schema for a rating system

rating table
rating_id (for uniqueness in case of same user_id, content_id, timestamp of a rating)
user_id str
content_id str
rating int (1 to 5)
timestamp (of the rating event, if a user has multiple for the same content_id we take most recent)

content table
content_id str
title str
content_type str


query for avg rating of each movie using only most recent rating per content

with ordered_ratings as (
    select content_id, user_id, rating, row_number() over (partition by content_id, user_id order by timestamp desc) as rn
    from rating
),
recent_ratings as (
    select *
    from ordered_ratings
    where rn = 1
)
select content_id, title, avg(rating) as avg_rating
from recent_ratings r
join content c
on r.content_id = c.content_id
where content_type = 'movie'
group by content_id, title
"""