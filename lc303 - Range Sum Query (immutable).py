# Given an integer array nums, find the sum of the
# elements between indices i and j (i ≤ j), inclusive.

# Example:
# Given nums = [-2, 0, 3, -5, 2, -1]
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
# Note:
# You may assume that the array does not change.
# There are many calls to sumRange function.

class SumRange:

    def __init__(self, nums):
        self.nums = nums
        self.hashmap = {}

    def sumRange(self, i, j):
        if (i,j) in self.hashmap.keys():
            return self.hashmap.get((i,j))
        else:
            total = 0
            for x in range(j - i + 1):
                total += self.nums[i + x]
                self.hashmap.update({(i,i + x): total})
        return total


obj = SumRange([-2, 0, 3, -5, 2, -1])
print(obj.sumRange(0,5))
print(obj.hashmap)


