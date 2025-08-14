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

# # Alternative solution using alias for cleaner code
# from pyspark.sql.functions import col

# # Using aliases for cleaner join syntax
# person_alias = person_df.alias("p")
# address_alias = address_df.alias("a")

# result_alternative = person_alias.join(
#     address_alias,
#     col("p.personId") == col("a.personId"),
#     "left"
# ).select(
#     col("p.firstName"),
#     col("p.lastName"),
#     col("a.city"),
#     col("a.state")
# )

# print("Alternative Solution Result:")
# result_alternative.show()

# # If you need to write to a file or table
# # result.write.mode("overwrite").parquet("path/to/output")

# # Stop Spark session
# spark.stop()


# # Function version for reusability
# def get_person_address_info(person_df, address_df):
#     """
#     Join Person and Address tables to get complete person information.
    
#     Args:
#         person_df: DataFrame with columns [personId, lastName, firstName]
#         address_df: DataFrame with columns [addressId, personId, city, state]
    
#     Returns:
#         DataFrame with columns [firstName, lastName, city, state]
#     """
#     return person_df.join(
#         address_df,
#         person_df.personId == address_df.personId,
#         "left"
#     ).select(
#         person_df.firstName,
#         person_df.lastName,
#         address_df.city,
#         address_df.state
#     )

# Example usage of the function
# result_func = get_person_address_info(person_df, address_df)
# result_func.show()


"""
given a list of intervals like [[1,6], [3,10], [3,3], [3,9], [1,4], [7,16], [17,22]]
representing viewed minutes of playback in a movie or video
write a function that takes these intervals and returns a list of intervals of all the unique minutes watched
there can be overlap in the input
"""

def mergeIntervals(intervals: [[int]]) -> [[int]]:
    # approach - we can do this by sorting on the first key and then merging all intervals together
    # this is an O(n log n) approach for the sort which dominates the time complexity
    # O(1) space though
    def merge(a, b):
        # [a1, a2], [b1, b2]
        if a[1] >= b[0]:
            return [a[0], max(a[1], b[1])]
        else:
            return None
    
    if not intervals:
        return []
        
    sorted_intervals = sorted(intervals)
    res = [sorted_intervals[0]]
    
    for i in range(1, len(sorted_intervals)):
        b = sorted_intervals[i]
        a = res[-1]
        
        merged = merge(a, b)
        if merged:
            res[-1] = merged
        else:
            res.append(b)
    
    return res

def mergeIntervals(intervals: [[int]]):
    # there's another approach here where we can trade some space for better time complexity
    # if these are movies / shows and we assume that it's bounded in run time, say 4 hours * 60 min = 480 max minutes
    # then we can use a boolean array and mark the indexes that are viewed, then generate a list of 
    # intervals that way without needing to sort
    minutes = [0] * 480
    for inter in intervals:
        a, b = inter
        for i in range(a, b):
            minutes[i] = 1
    
    res = []
    idx = 0

    while idx < len(minutes):
        if minutes[idx] == 1:
            start = idx
            while i < len(minutes) and minutes[idx] == 1:
                idx += 1
            # at this point idx has reached end of a sequence of 1s
            res.append([start, idx])
        else:
            idx += 1

    return res


ints = [[24, 29], [1,6], [3,10], [3,3], [3,9], [1,4], [7,16], [17,22], [30, 31]]
print(mergeIntervals(ints))