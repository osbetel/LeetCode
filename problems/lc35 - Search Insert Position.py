




def searchInsert(nums, target):
    # given a sorted array of distinct integers, return index of target,
    # otherwise return index where it would be if inserted!
    # -> binary search
    # -> return if found
    # -> else return that index anyways
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        elif target < nums[mid]:
            right = mid - 1
    if nums[mid] < target:
        return mid + 1
    else:
        return mid # no need to -1 due to floor division


nums = [2,3,5,6]
target = 4
print(searchInsert(nums, target))




