from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("PersonAddressQuery") \
    .getOrCreate()

# Create sample data for Person table
person_data = [
    (1, "Wang", "Allen"),
    (2, "Alice", "Bob")
]

person_columns = ["personId", "lastName", "firstName"]
person_df = spark.createDataFrame(person_data, person_columns)

# Create sample data for Address table
address_data = [
    (1, 2, "New York City", "New York"),
    (2, 3, "Leetcode", "California")
]

address_columns = ["addressId", "personId", "city", "state"]
address_df = spark.createDataFrame(address_data, address_columns)

# Display input tables
print("Person Table:")
person_df.show()

print("Address Table:")
address_df.show()

# Solution: LEFT JOIN to get all persons with their addresses (if they exist)
result = person_df.join(
    address_df,
    person_df.personId == address_df.personId,
    "left"  # LEFT JOIN ensures all persons are included
).select(
    person_df.firstName,
    person_df.lastName,
    address_df.city,
    address_df.state
)

print("Result:")
result.show()

# Alternative solution using alias for cleaner code
from pyspark.sql.functions import col

# Using aliases for cleaner join syntax
person_alias = person_df.alias("p")
address_alias = address_df.alias("a")

result_alternative = person_alias.join(
    address_alias,
    col("p.personId") == col("a.personId"),
    "left"
).select(
    col("p.firstName"),
    col("p.lastName"),
    col("a.city"),
    col("a.state")
)

print("Alternative Solution Result:")
result_alternative.show()

# If you need to write to a file or table
# result.write.mode("overwrite").parquet("path/to/output")

# Stop Spark session
spark.stop()


# Function version for reusability
def get_person_address_info(person_df, address_df):
    """
    Join Person and Address tables to get complete person information.
    
    Args:
        person_df: DataFrame with columns [personId, lastName, firstName]
        address_df: DataFrame with columns [addressId, personId, city, state]
    
    Returns:
        DataFrame with columns [firstName, lastName, city, state]
    """
    return person_df.join(
        address_df,
        person_df.personId == address_df.personId,
        "left"
    ).select(
        person_df.firstName,
        person_df.lastName,
        address_df.city,
        address_df.state
    )

# Example usage of the function
# result_func = get_person_address_info(person_df, address_df)
# result_func.show()