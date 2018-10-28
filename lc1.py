

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.

# Example:
# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


def twoSum(nums, target):
    values = {}
    for i in range(0, len(nums)):
        diff = target - nums[i]
        if values.__contains__(diff):
            return [values.get(diff), i]
        values.update({nums[i]: i})

    return -1
    # for i in range(0, len(nums)):
    #     if nums[i] > abs(target):
    #
    #         continue
    #     for j in range(i, len(nums)):
    #         if nums[i] + nums[j] == target and i != j:
    #             return [i,j]




print(twoSum([2,7,11,15],9))          # [0,1]
print(twoSum([3,2,4], 6))             # [1,2]
print(twoSum([0,4,3,0],0))            # [0,3]
print(twoSum([-1,-2,-3,-4,-5],-8))    # [2,4]
print(twoSum([-3,4,3,90],0))          # [0,2]
print(twoSum([3,2,95,4,-3],92))       # [2,4]


