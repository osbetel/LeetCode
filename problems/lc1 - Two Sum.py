

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.

# Example:
# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    seen_pair = {} # where k is y = target - x, and v is the index of y
    for i in range(len(nums)):
        x = nums[i]
        y = target - x
        # found the corresponding pair for x => x + y = target
        if y in seen_pair:
            return [i, seen_pair[y]]
        else:
            seen_pair[x] = i


import time
start = time.time_ns()
tests = [
    [[2,7,11,15],9],          # [0,1]
    [[3,2,4], 6],             # [1,2]
    [[0,4,3,0],0],            # [0,3]
    [[-1,-2,-3,-4,-5],-8],    # [2,4]
    [[-3,4,3,90],0],          # [0,2]
    [[3,2,95,4,-3],92],       # [2,4]
]
for t in tests:
    print(twoSum(*t))
# print(time.time_ns() - start)


