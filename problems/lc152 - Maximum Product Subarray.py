


def maxProdSubArray(nums):
    # kadane
    if len(nums) == 0:
        return None
    maximum = nums[0]
    for i in range(1, len(nums)):
        if nums[i - 1] != 0:
            nums[i] = max(nums[i] * nums[i - 1], nums[i])
        if nums[i] > maximum:
            maximum = nums[i]
        # print(nums)
    return maximum


n = ([2,3,-2,4], [-2,0,-1], [-1,-1,-10,1,1,1,1,-50], [0, 2], [3,-1,4])
s = (6,0,500,2,4)
for k in n:
    print(maxProdSubArray(k))

