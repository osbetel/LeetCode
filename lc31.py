# Implement next permutation, which rearranges numbers into the
# lexicographically next greater permutation of numbers.
#
# If such arrangement is not possible, it must rearrange it as
# the lowest possible order (ie, sorted in ascending order).
#
# The replacement must be in-place and use only constant extra memory.
#
# Here are some examples. Inputs are in the left-hand column and
# its corresponding outputs are in the right-hand column.
#
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1

import sys
def nextPermutation(nums: [int]):

    if nums == []:
        return
    if len(nums) == 2:
        nums.reverse()
    else:
        nextNum(nums)


def nextNum(nums: [int]):

    if inGreatestForm(nums):
        nums.reverse()
        return

    smallest = -1
    idx = -1
    for i in range(len(nums) - 1, 0, -1):
        # find the first decrease from a[i] to a[i - 1]
        if nums[i] > nums[i - 1]:
            smallest = nums[i - 1]
            idx = i - 1
            # print(nums[i], smallest)
            break

    # now idx is the index of the smallest from the right,
    # and smallest is the value
    idj = idx + 1
    diff = sys.maxsize
    for j in range(idx, len(nums)):
        if nums[j] > smallest and (nums[j] - smallest) <= diff:
            # essentially we are walking forwards from idx
            # and finding the value with the smallest difference to idx
            diff = nums[j] - smallest
            idj = j

    tmp = nums[idj]
    nums[idj] = smallest
    nums[idx] = tmp

    inPlaceReverse(nums, idx + 1, len(nums) - 1)

    return


def inPlaceReverse(nums: [int], front, back):
    # print(nums, front, back)
    while front < back:
        tmp = nums[front]
        nums[front] = nums[back]
        nums[back] = tmp
        front += 1
        back -= 1


def inGreatestForm(nums: [int]):
    # return true if list is in greatest form,
    # false otherwise
    great = True
    for i in range(len(nums) - 1):
        great &= (nums[i] >= nums[i + 1])
    return great


t1 = [
    [1,2,3],        # [1,3,2]
    [3,2,1],
    [1,1,5]
]
t2 = [
    [9,1,7,4,5],    # [9,1,7,5,4]
    [8,2,6,5,1],    # [8,5,1,2,6]
    [9,8,7,4,3]     # [3,4,7,8,9]
]
t3 = [
    [2,1,2,2,1]     # [2,2,1,1,2]
]
t4 = [
    [4,2,0,2,3,2,0]     # [4,2,0,3,0,2,2]
]

def test(ks):
    for k in ks:
        nextPermutation(k)
        print(k)


# test(t1)
# test(t2)
# test(t3)
# test(t4)
m = [1,3,2]
nextPermutation(m)
print("final: " + str(m))


