# from pyspark.sql import SparkSession
# from pyspark.sql.functions import col

# # Initialize Spark Session
# spark = SparkSession.builder \
#     .appName("PersonAddressQuery") \
#     .getOrCreate()

# # Create sample data for Person table
# person_data = [
#     (1, "Wang", "Allen"),
#     (2, "Alice", "Bob")
# ]

# person_columns = ["personId", "lastName", "firstName"]
# person_df = spark.createDataFrame(person_data, person_columns)

# # Create sample data for Address table
# address_data = [
#     (1, 2, "New York City", "New York"),
#     (2, 3, "Leetcode", "California")
# ]

# address_columns = ["addressId", "personId", "city", "state"]
# address_df = spark.createDataFrame(address_data, address_columns)

# # Display input tables
# print("Person Table:")
# person_df.show()

# print("Address Table:")
# address_df.show()

# # Solution: LEFT JOIN to get all persons with their addresses (if they exist)
# result = person_df.join(
#     address_df,
#     person_df.personId == address_df.personId,
#     "left"  # LEFT JOIN ensures all persons are included
# ).select(
#     person_df.firstName,
#     person_df.lastName,
#     address_df.city,
#     address_df.state
# )

# print("Result:")
# result.show()


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

from pyspark.sql import SparkSession

# first create spark session
spark = (
    SparkSession.builder
    .appName("audio_processing")
    .getOrCreate()
)

# now need to get source data, should be (key, url)
data = [
    (1, "https://www.youtube.com/watch?v=NAP-KRCyLv4"),   # martin garrix sleepless night
    (2, "https://www.youtube.com/watch?v=Gjxm1s26dXY"),   # martin garrix carry you
    (3, "https://www.youtube.com/watch?v=zw47ymC0RNQ"),   # saib in your arms
    (4, "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),   # rick roll
    (5, "https://www.youtube.com/watch?v=kJQP7kiw5Fk"),   # despacito
    (6, "https://www.youtube.com/watch?v=9bZkp7q19f0"),   # gangnam style
    (7, "https://www.youtube.com/watch?v=YQHsXMglC9A"),   # hello adele
    (8, "https://www.youtube.com/watch?v=hT_nvWreIhg"),   # counting stars
]

columns = ["song_id", "url"]

df = spark.createDataFrame(data, columns)
df.show()



