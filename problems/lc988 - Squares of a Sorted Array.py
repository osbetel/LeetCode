



def findFirstPositiveNum(nums):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid - 1] < 0 <= nums[mid]:
            return mid
        elif nums[mid] < 0:
            left = mid + 1
        elif 0 <= nums[mid]:
            right = mid - 1
    # list is all positives or all negatives
    if nums[0] < 0:
        return -1
    else:
        return 0

def sortedSquares(nums):
    # array of sorted non-decreasing integers
    # return an array of the squares of each number
    # could square everything and sort, O(n + (n log n)) -> O(n log n) though, not the best. O(n) possible?
    # note that the array is non-decreasing!
    # -> find the first positive number with binary search O(log n)
    # -> square all positive numbers and square all negative numbers separately
    # -> we can iterate over this like we would iterate over two lists -> O(n)
    if len(nums) == 1:
        return [nums[0] ** 2]
    first_positive = findFirstPositiveNum(nums)
    left = nums[:first_positive]
    right = nums[first_positive:]
    left = [x**2 for x in left]
    right = [x**2 for x in right]
    res = []
    while left and right:
        print(left, right, res)
        if left[-1] < right[0]:
            res.append(left.pop(-1))
        elif left[-1] > right[0]:
            res.append(right.pop(0))
        else:
            res.append(left.pop(-1))
            res.append(right.pop(0))
    print(left, right, res)
    if left:
        res.extend(reversed(left))
    if right:
        res.extend(right)
    return res

nums = [-5,-5,-4,-3,-2,-1]
print(sortedSquares(nums))
