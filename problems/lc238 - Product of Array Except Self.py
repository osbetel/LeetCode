









def productExceptSelf(nums):
    # no dividing allowed
    # [1,2,3,4] -> [24, 12, 8, 6]
    left = [1] * len(nums)
    for i in range(1, len(nums)):
        left[i] = left[i - 1] * nums[i - 1]

    right = [1] * len(nums)
    for i in reversed(range(0, len(nums) - 1)):
        right[i] = right[i + 1] * nums[i + 1]

    # print(left)
    # print(right)
    return [x * y for x, y in zip(left, right)]

k = [1,2,3,4]
print(productExceptSelf(k))

