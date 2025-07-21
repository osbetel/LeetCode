# You are given an integer array nums and an integer target.
#
# You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.
#
# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
# Return the number of different expressions that you can build, which evaluates to target.
# Input: nums = [1,1,1,1,1], target = 3
# Output: 5
# Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3
#
# 1) recursion + memoization
# 2) table filling

memo = {}
def findTargetSumWays(nums, S):
    index = len(nums) - 1
    curr_sum = 0
    return dp(nums, S, index, curr_sum)


def dp(nums, target, index, curr_sum):
    global memo
    # working backwards. Start at last index and backtrack
    # base case, if checked before, return cached result
    if (index, curr_sum) in memo:
        return memo[(index, curr_sum)]

    # other base cases ->
    # 1) index is less than 0 AND we've reached our target (ie all numbers have been used)
    # 2) index is less than 0 and we have NOT reached the target
    if index < 0 and curr_sum == target:
        return 1
    if index < 0:
        return 0

    # recursion: check with addition and subtraction recursively
    positive = dp(nums, target, index - 1, curr_sum + nums[index])
    negative = dp(nums, target, index - 1, curr_sum + -nums[index])

    # add to cache
    memo[(index, curr_sum)] = positive + negative
    return memo[(index, curr_sum)]

k = [1]
t = 1
print(findTargetSumWays(k, t))



