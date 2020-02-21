# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
# You may assume nums1 and nums2 cannot be both empty.
# TODO: incomplete because I'm lazy
def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    # approach: how do we solve this in log(m + n) time? First, consider how we can solve the median of a list in
    # log(n) time... You jump right to the middle with a binary "search" (really just access the middle element,
    # 1 element if list size is odd, middle 2 if it's even) and return the median.
    # in order to do two lists we need to perform this binary search on both lists at the same time.
    # this gets a little more complex...
    m, n = len(nums1), len(nums2)


def klogkFindMedianSortedArrays(nums1, nums2):
    # this one works lol, but it's in O((m + n)*log(m + n)) time. Which, for smaller sized arrays is not bad.
    # also important to note that 
    AplusB = nums1 + nums2
    AplusB.sort()
    l = len(AplusB)
    if l % 2 != 0:
        return AplusB[l // 2]
    else:
        return (AplusB[(l // 2) - 1] + AplusB[l // 2]) / 2




def test1():
    nums1 = [1, 3]
    nums2 = [2]
    return findMedianSortedArrays(nums1, nums2)


def test2():
    nums1 = [1, 2]
    nums2 = [3, 4]
    return findMedianSortedArrays(nums1, nums2)


def test3():
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [3, 4, 7, 9, 10]
    return findMedianSortedArrays(nums1, nums2)


def test4():
    nums1 = [2]
    nums2 = []
    return findMedianSortedArrays(nums1, nums2)


def test5():
    nums1 = [1,2,3,4]
    nums2 = [3,4,5,6]
    return findMedianSortedArrays(nums1, nums2)


def test6():
    nums1 = []
    nums2 = [2,3]
    return findMedianSortedArrays(nums1, nums2)


def test7():
    nums1 = [1]
    nums2 = [2,3]
    return findMedianSortedArrays(nums1, nums2)


def test8():
    nums1 = [1]
    nums2 = [2,3,4]
    return findMedianSortedArrays(nums1, nums2)

assert test1() == 2 # 2
assert test2() == 2.5 # 2.5
assert test3() == 4 # 4
assert test4() == 2 # 2
assert test5() == 3.5 # 3.5
assert test6() == 2.5 # 2.5
assert test7() == 2 # 2
assert test8() == 2.5 # 2.5




