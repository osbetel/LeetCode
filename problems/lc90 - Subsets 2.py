"""
given an integer array nums that may contain duplicates, return the powerset (all possible subsets)
"""

from typing import List
def subsetsWithDup_recursive(nums: List[int]) -> List[List[int]]:
    nums.sort()
    result = []
    
    def backtrack(start, path):
        result.append(path[:])
        
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    
    backtrack(0, [])
    return result


def subsetsWithDup_iterative(nums: List[int]) -> List[List[int]]:
    nums.sort()
    result = [[]]
    
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            new_subsets = []
            for j in range(len(result) - prev_size, len(result)):
                new_subsets.append(result[j] + [nums[i]])
        else:
            prev_size = len(result)
            new_subsets = []
            for subset in result:
                new_subsets.append(subset + [nums[i]])
        result.extend(new_subsets)
    
    return result

tests = [
    [1,2,2]
]
for t in tests:
    print(subsetsWithDup_recursive(t))