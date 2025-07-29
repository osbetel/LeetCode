"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true
Explanation:
The element 1 occurs at the indices 0 and 3.

Example 2:
Input: nums = [1,2,3,4]
Output: false
Explanation:
All elements are distinct.

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

from typing import List
def containsDuplicate(nums: List[int]) -> bool:
    # return true if any duplicate elements, return false if every element is distinct
    # approach - can keep track of values seen with a set, if a new element is found in the set, return True. O(n) time, O(n) space
    # is there potentially a way to do it without any space? yes, but we'd need to sort in-place which is O(n log n) and then iterate over 
    # with a sliding window of size two. If at any time that window is [x, x] then we have duplicates
    seen = set()
    for x in nums:
        if x in seen:
            return True
        else:
            seen.add(x)
    return False
    # can also do this code with a one-liner which is faster. set creation happens in C and is thus faster at the compiler / interpreter level.
    # len(nums) != len(set(nums))
    


tests = [
    [1,2,3,1],
    [1,2,3,4],
    [1,1,1,3,3,4,3,2,4,2],
]
for t in tests:
    print(containsDuplicate(t))