




"""
Given a list of integers and a target, return all triplets of integers where they add up to a target sum
duplicate elements not allowed. duplicate sets of integers not allowed
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Distinct sets are the ones in order from least to greatest
"""


def twoSum(nums, target, idx):
    i = idx
    j = len(nums) - 1
    while i < j:
        s = nums[i] + nums[j]
        if s == target:
            return True

        if s < target:
            i += 1
        else:
            j -= 1

    return False


def threeSum(arr, required_sum):
  arr.sort()
  for i in range(0, len(arr)-2):
    remaining_sum = required_sum - arr[i]
    if twoSum(arr, remaining_sum, i+1):
      return True

  return False


def threeSum(nums: [int], target: int = 0) -> [[int]]:
    """
    approach? I guess the naive way would be to generate every combination of integers from the list,
    check all of them. return the ones that meet the target.
    is there a better way to run through all of these? Can we cut down on the number of combinations we need to try?

    triple while loop was too slow. can we sort and use binary search?
    """


    N = len(nums)
    if N < 3:
        return []
    x, y, z = 0, 1, 2
    res = set()

    nums.sort()
    # print(nums)

    # x + y + z = target
    # target - x = y + z
    # target - x - y = z

    while x < N:
        yzt = target - nums[x]  # y + z must sum up to this value
        while y < N:
            zt = yzt - nums[y]  # z must be this value for this value of y
            z = binarySearch(nums[y:], zt)
            # while z < N:
            # if nums[z] == zt:
            res.add(tuple(sorted([nums[x], nums[y], nums[z]])))
                # z += 1
            y += 1
            # z = y + 1
        x += 1
        y = x + 1
        # z = x + 2

    res = [list(x) for x in list(res)]
    return res

k = threeSum([-1,0,1,2,-1,-4])
print(k)
