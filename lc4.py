
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
# You may assume nums1 and nums2 cannot be both empty.
# TODO: Incomplete LC4
def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """

    # let a be a pointer to the first element of nums1
    # and b be a pointer to the first element of nums2

    if len(nums1) + len(nums2) == 0: return None

    if len(nums1) == 0 and len(nums2) != 0:
        # just get the median of nums2 then
        l = len(nums2)
        if l % 2 == 0:
            return (nums2[int(l/2)] + nums2[int(l/2 - 1)]) / 2
        else:
            return nums2[int(l/2)]

    if len(nums2) == 0 and len(nums1) != 0:
        # just get the median of nums2 then
        l = len(nums1)
        if l % 2 == 0:
            return (nums1[int(l/2)] + nums1[int(l/2 - 1)]) / 2
        else:
            return nums1[int(l/2)]

    totalLen = len(nums1) + len(nums2)
    target = totalLen / 2
    fractional = str(target).__contains__(".5")
    if fractional: target = round(target)
    a = 0
    b = 0

    while (a + b) < target - 1:

        if nums1[a] < nums2[b]:
            a += 1
        elif nums1[a] == nums2[b]:
            a += 1
            b += 1
        elif nums2[b] < nums1[a]:
            b += 1
        # print(a,b, target)
    if not fractional:
        return (nums1[a] + nums2[b]) / 2
    else:
        if a >= len(nums1):
            return nums2[b]
        elif b >= len(nums2):
            return nums1[a]
        return min(nums1[a], nums2[b])



def test1():
    nums1 = [1, 3]
    nums2 = [2]
    print(findMedianSortedArrays(nums1, nums2))


def test2():
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(findMedianSortedArrays(nums1, nums2))


def test3():
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [3, 4, 7, 9, 10]
    print(findMedianSortedArrays(nums1, nums2))


def test4():
    nums1 = [2]
    nums2 = []
    print(findMedianSortedArrays(nums1, nums2))


def test5():
    nums1 = [1,2,3,4]
    nums2 = [3,4,5,6]
    print(findMedianSortedArrays(nums1, nums2))


def test6():
    nums1 = []
    nums2 = [2,3]
    print(findMedianSortedArrays(nums1, nums2))


def test7():
    nums1 = [1]
    nums2 = [2,3]
    print(findMedianSortedArrays(nums1, nums2))


def test8():
    nums1 = [1]
    nums2 = [2,3,4]
    print(findMedianSortedArrays(nums1, nums2))

# test1() # 2
# test2() # 2.5
# test3() # 4
# test4() # 2
# test5() # 4
# test6() # 2.5
# test7() # 2
test8() # 2.5


