


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

def maxSubArrayDP(nums):
    return maxSubArray(nums)
    n = len(nums)
    dp = [0] * n # where dp[i] is the max subarray ending at index nums[i]
    maximum = dp[0]
    for i in range(1, n):
        if dp[i - 1] > 0:
            dp[i] = nums[i] + dp[i - 1]
        else:
            dp[i] = nums[i] + 0
    return maximum




def s2():
    import random as rand
    k = []
    for x in range(0, 1000):
        k.append(rand.randint(-100000, 100000))
    print(maxSubArray(k))

print(maxSubArrayDP([-2,1,-3,4,-1,2,1,-5,4])) # 6
print(maxSubArrayDP([-214124,-12489]))        # -12489
print(maxSubArrayDP([]))                      # None
print(maxSubArrayDP([9]))                     # 9
print(maxSubArrayDP([214478352,-2144783523])) # 2144783523
print(maxSubArrayDP([-2,-1]))                 # -1
print(maxSubArrayDP([-2,1]))                  # 1
print(maxSubArrayDP([1,2]))                   # 3
print(maxSubArrayDP([1,-1,-2]))               # 1




