




def search(nums: [int], target: int) -> int:
    # given an array of integers sorted in ascending order, and a target, find the
    # index of target. If not exists, return -1
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        elif target < nums[mid]:
            right = mid - 1
    return -1

nums = [-1,0,3,5,9,12]
target = 12

print(search(nums, target))



