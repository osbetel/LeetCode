
# Suppose a robot is located at the top left corner of an m x n grid.
# The robot can only move right or down at any given point.
# The goal is to reach the bottom right corner of the grid
# How many unique paths are there to get to the bottom?


import math
def uniquePaths(m, n):
    # Output the number of unique paths.
    # Example, m = 3, n = 2, then paths = 3
    # m = 7, n = 3, then paths =  28

    if m == 0 or n == 0: return 0
    if m == 1 or n == 1: return 1
    return int(math.factorial(m + n - 2) / (math.factorial(m - 1) * math.factorial(n - 1)))

















