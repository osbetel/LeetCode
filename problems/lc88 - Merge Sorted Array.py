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
    # approach - [1,2,5,0,0,0], [2,5,6]. O(m + n) time, O(1) space
    # take this example. We usde a three pointer approach, left, right, and insert.
    # left = last element of nums1 (that is non zero)
    # right = last element of nums2
    # insert = last index in nums1 (will be a zero)
    # then while the right pointer > -1
    # 1) if left_val <= right_val -> insert right value to insertion pointer, decrement right and insert
    # 2) if left val > right_val, insert left value to insertion pointer, decrement left and insert
    if not nums2:
        return nums1

    left = m - 1  # last element of nums1
    right = n - 1  # last element of nums2
    insert = m + n - 1  # end of nums1

    # what are the conditions for a swap?
    # for i in range(10):
    # while right > -1:
    #     left_val = nums1[left] if left > 0 else -1
    #     right_val = nums2[right] if right > 0 else -1
    #     print(left, right, insert, nums1, nums2)
    #     if left_val <= right_val:
    #         nums1[insert] = nums2[right]
    #         right -=1
    #         insert -=1
    #     elif left_val > right_val:
    #         nums1[insert] = nums1[left]
    #         insert -= 1
    #         left -= 1
    # return nums1

    while right >= 0:
        # nums1 exhausted or nums2 element is larger, insert from nums2, else nums1
        if left < 0 or nums2[right] > nums1[left]:
            nums1[insert] = nums2[right]
            right -= 1
        else:
            nums1[insert] = nums1[left]
            left -= 1
        insert -= 1

    return nums1


def mergeBruteForce(nums1, m, nums2, n):
    # how would we approach this in the brute force scenario?
    # 1) could just combine lists and then do an in-place sort?
    
    # approach 1, merge arrays and then sort
    # this is O(n log n)
    insert = m
    for i in range(n):
        nums1[insert] = nums2[i]
        insert += 1
    nums1.sort()
    return nums1


def mergeTwoPointer(nums1, m, nums2, n):
    # approach 3: two-pointer with extra space
    # copy nums1 to auxiliary array, then merge from beginning
    # O(m+n) time, O(m) space
    
    nums1_copy = nums1[:m]  # copy only the elements that are not zeros

    # now we can approach this like merging two sorted arrays with pointers with nums1 as the output array
    left = 0
    right = 0
    insert = 0
    while insert < m + n:
        left_val = nums1_copy[left] if left < m else -1
        right_val = nums2[right] if right < n else -1
        # print(left, right, insert, nums1_copy, nums2, nums1)
        if left_val <= right_val and left < m:
            nums1[insert] = left_val
            left += 1
        elif right < n:
            nums1[insert] = right_val
            right += 1
        else:
            print("spork")
            break
        insert += 1
        
    return nums1

test_cases = [
    ([1,2,5,0,0,0], 3, [2,5,6], 3),
    ([2,2,7,0,0,0], 3, [5,5,7], 3),
    ([1] , 1, [], 0),
    ([0],0 ,[1], 1),
    ([2, 0], 1, [1], 1)
]

for t in test_cases:
    print(merge(*t))