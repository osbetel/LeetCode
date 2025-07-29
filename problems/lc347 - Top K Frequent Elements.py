"""
Given an integer array nums and an integer k, return the k 
most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
"""

from typing import List
def topKFrequent(nums: List[int], k) -> List[int]:
    # approach - iterate through, get a hashmap of characters and their frequencies
    # sort dictionary by value
    # return top k keys
    # O(n) time

    counts = {}
    for x in nums:
        counts[x] = counts.get(x, 0) + 1
    
    frequencies = sorted([(k, v) for k, v in counts.items()], key=lambda x: x[1], reverse=True)
    print(frequencies)
    return [x[0] for x in frequencies][:k]

tests = [
    ([1,1,1,2,2,3], 2)
]
for t in tests:
    print(topKFrequent(*t))