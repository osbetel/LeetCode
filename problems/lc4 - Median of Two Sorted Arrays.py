import random
import numpy as np

# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
# You may assume nums1 and nums2 cannot be both empty.
def findMedianSortedArrays(l1, l2):
    # approach: how do we solve this in log(m + n) time? First, consider how we can solve the median of a list in
    # log(n) time... You jump right to the middle with a binary "search" (really just access the middle element,
    # 1 element if list size is odd, middle 2 if it's even) and return the median.
    # in order to do two lists we need to perform this binary search on both lists at the same time.
    m, n = len(l1), len(l2)
    total_length = m + n
    median_index = total_length // 2  # check later if even or odd
    previous_num = -1
    m, n = 0, 0
    while m + n < median_index:
        if l1[m] > l2[n]:
            previous_num = l2[n]
            if n == len(l2):
                m += 1
            else:
                n += 1
            median = l2[n]
        elif l1[m] < l2[n]:
            previous_num = l1[m]
            if m == len(l1):
                n += 1
            else:
                m += 1
            median = l1[m]
        elif l1[m] == l2[n]:
                previous_num = l1[m]
                if m == len(l1):
                    n += 1
                else:
                    m += 1
                median = l1[m]
        print(m, n, median_index)
        if m + n >= median_index:
            break

    if total_length % 2 == 0:
        print("EVEN")
        median = median + previous_num
        median /= 2
    print(l1, l2)
    print(sorted(l1 + l2))
    return median




def klogkFindMedianSortedArrays(nums1, nums2):
    # this one works lol, but it's in O((m + n)*log(m + n)) time. Which, for smaller sized arrays is not bad.
    AplusB = nums1 + nums2
    AplusB.sort()
    l = len(AplusB)
    if l % 2 != 0:
        return AplusB[l // 2]
    else:
        return (AplusB[(l // 2) - 1] + AplusB[l // 2]) / 2


def generateTestArray():
    m = random.randint(2, 5)
    n = random.randint(2, 5)
    l1 = []
    l2 = []
    for i in range(m):
        l1.append(random.randint(0, 10))
    for i in range(n):
        l2.append(random.randint(0, 10))
    return sorted(l1), sorted(l2)

X, Y = generateTestArray()

try:
    k = findMedianSortedArrays(X, Y)
    print(k)
except Exception as e:
    print(e)
    print(X, Y)

print(f"numpy: {np.median(X + Y)}")
