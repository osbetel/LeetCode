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
        
        r += l1[i:]
        r += l2[j:]
        return r

    L = combineSortedLists(l1, l2)
    if len(L) % 2 == 0:
        left = len(L) // 2 - 1
        right = len(L) // 2
        median = (L[left] + L[right]) / 2
    else:
        left = len(L) // 2
        median = L[left]
    return median


def findMedianSortedArraysOptimal(nums1, nums2):
    # Ensure nums1 is the smaller array
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    m, n = len(nums1), len(nums2)
    left, right = 0, m
    
    while left <= right:
        # Partition nums1
        i = (left + right) // 2
        # Partition nums2 such that left side has (m+n+1)//2 elements
        j = (m + n + 1) // 2 - i
        
        # Get boundary elements (use -inf/inf for edge cases)
        maxLeft1 = float('-inf') if i == 0 else nums1[i-1]
        minRight1 = float('inf') if i == m else nums1[i]
        
        maxLeft2 = float('-inf') if j == 0 else nums2[j-1]
        minRight2 = float('inf') if j == n else nums2[j]
        
        # Check if partition is valid
        if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
            # Found correct partition
            if (m + n) % 2 == 0:
                return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
            else:
                return max(maxLeft1, maxLeft2)
        elif maxLeft1 > minRight2:
            # i is too large, move left
            right = i - 1
        else:
            # i is too small, move right
            left = i + 1


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
k = findMedianSortedArrays(X, Y)
print(k)
