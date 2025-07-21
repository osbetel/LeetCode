import random
import numpy as np

# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays.
# You may assume nums1 and nums2 cannot be both empty.
def findMedianSortedArrays(l1, l2):
    # approaches:
    # 1) can combine two sorted lists in O(n) time and then find the median in O(log(n)) time
    # 2) there is a way to do in O(log(n + m)) time
    def combineSortedLists(l1, l2):
        i, j = 0, 0
        r = []
        while i < len(l1) and j < len(l2):
            a = l1[i]
            b = l2[j]
            if a < b:
                r.append(a)
                i += 1
            else:
                r.append(b)
                j += 1
        return r

    L = combineSortedLists(l1, l2)
    print(L)
    if len(L) % 2 == 0:
        left = len(L) // 2 - 1
        print(left)
        right = len(L) // 2
        print(right)
        median = (L[left] + L[right]) / 2
    else:
        left = len(L) // 2
        print(left)
        median = L[left]
    print(median)


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
