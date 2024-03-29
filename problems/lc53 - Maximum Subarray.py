


# Given an integer array nums, find the contiguous subarray (containing at least
# one number) which has the largest sum and return the sum.
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.


from sys import maxsize
def maxSubArray1(nums: [int]):

    if len(nums) == 0: return None
    if len(nums) == 1: return nums[0]

    l = len(nums)
    s = 0
    maxi = nums[0]
    # maxi = -maxsize
    sums = []

    for i in range(0, l):
        s += nums[i]
        sums.append(s)
        if maxi < s:
            maxi = s
        if s < 0:
            s = 0
    # print(sums, maxi)

    return maxi

def maxSubArray2(nums):
    if len(nums) == 0: return None
    if len(nums) == 1: return nums[0]
    maximum = nums[0]
    partial_sum = 0
    sums = []
    for i in range(len(nums)):
        partial_sum += nums[i]
        sums.append(partial_sum)
        print(partial_sum)
        if maximum < partial_sum:
            maximum = partial_sum
        if partial_sum < 0:
            partial_sum = 0
    return maximum

def maxSubArray(nums):
    # kadane
    if len(nums) == 0:
        return None
    maximum = nums[0]
    for i in range(1, len(nums)):
        if nums[i - 1] > 0:
            nums[i] += nums[i - 1]
        if nums[i] > maximum:
            maximum = nums[i]
        # print(nums)
    return maximum



def s2():
    import random as rand
    k = []
    for x in range(0, 1000):
        k.append(rand.randint(-100000, 100000))
    print(maxSubArray(k))

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) # 6
print(maxSubArray([-214124,-12489]))        # -12489
print(maxSubArray([]))                      # None
print(maxSubArray([9]))                     # 9
print(maxSubArray([214478352,-2144783523])) # 2144783523
print(maxSubArray([-2,-1]))                 # -1
print(maxSubArray([-2,1]))                  # 1
print(maxSubArray([1,2]))                   # 3
print(maxSubArray([1,-1,-2]))               # 1




