


def maxProdSubArray(nums):
    # kadane
    if len(nums) == 0:
        return None
    maximum = nums[0]
    count_negatives = 0
    for x in nums:
        if x < 0:
            count_negatives += 1
    count_negatives = count_negatives % 2  # if 0, even number of negatives, consider absolute values

    for i in range(1, len(nums)):
        if count_negatives == 0:
            a, b = abs(nums[i-1]), abs(nums[i])
        else:
            a, b = nums[i-1], nums[i]

        # print(nums)
        if a != 0:
            b = max(b * a, b)
        if b > maximum:
            maximum = b
    return maximum

def maxProduct(nums) -> int:
    # approach:
    # single pass iteration
    # track max and min, why min? because we need to consider negative numbers too, and -100000 can be greater than 9000
    # if we encounter a -1 later on for example
    curMax, curMin = 1, 1
    res = nums[0] # save global maximum

    for n in nums:
        vals = (n, n * curMax, n * curMin)
        curMax, curMin = max(vals), min(vals)
        res = max(res, curMax)

    return res

n = ([2,3,-2,4], [-2,0,-1], [-1,-1,-10,1,1,1,1,-50], [0, 2], [3,-1,4])
s = (6,0,500,2,4)
for k in n:
    print(maxProduct(k))

