"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should 
be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
"""

from typing import List
def merge(
    nums1: List[int],
    m: int,
    nums2: List[int],
    n: int
):
    # so nums1 has a length of m + n guarnateed, and it has m digits
    # arrays in non decreasing sort order
    # approach? we can do a sort of bubble sort? Iterate over nums2 and insert elements into nums1 based? This would require multiple
    # for loops over nums1 though so O(n^2) worst case.
    # better way? we can have two pointers, one at the front of each array.
    # while loop -> we move the left pointer up until left value is greater than right value
    # -> then we swap elements
    # -> continue this process until left value is less than right value and then swap
    # -> increment right pointer, repeat to end
    if not nums2:
        return nums1

    def swap(i, j, a1, a2):
        # swap elements a1[i] <=> a2[j]
        temp = a1[i]
        a1[i] = a2[j]
        a2[j] = temp

    left = 0
    right = 0

    # what are the conditions for a swap?
    # 1) while we are in the bounds of left < m, if left_val > right_val, swap

    while left < m:
        left_val = nums1[left]
        right_val = nums2[right]
        if left_val > right_val:
            swap(left, right, nums1, nums2)
            left +=1
        else:
            left += 1

    # at this point, the left array has been exhausted, append right array, account for 0s 
    for i in range(left, m + n):
        swap(left, right, nums1, nums2)
        left_val = nums1[left]
        right_val = nums2[right]
        if right_val == 0:
            right += 1
        elif left_val == 0:
            left += 1
        else:
            left += 1

    if left_val == 0:
        swap(left, right, nums1, nums2)

    print(left, right, nums1, nums2, m)

    return nums1


test_cases = [
    # ([1,2,5,0,0,0], 3, [2,5,6], 3),
    ([2,2,7,0,0,0], 3, [5,5,7], 3),
    # ([1] , 1, [], 0),
    # ([] , 0, [1], 1),
    # ([0],0 ,[1], 1)
]

for t in test_cases:
    print(merge(*t))