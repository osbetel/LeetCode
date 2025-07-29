import random
import numpy as np

# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays.
# You may assume nums1 and nums2 cannot be both empty.
def findMedianSortedArrays(l1, l2):
    # approach - there's an easy and somewhat efficient approach
    # we can combine two sorted arrays in O(n) time and then find the median instantly
    
    def combineSortedArrays(a1, a2):
        l = []
        left, right = 0, 0
        while left < len(a1) or right < len(a2):
            left_val = a1[left] if left < len(a1) else 10 ** 10
            right_val = a2[right] if right < len(a2) else 10 ** 10

            # put the smaller element in the result array and increment its pointer
            if left_val < right_val:
                l.append(left_val)
                left += 1
            else:
                l.append(right_val)
                right += 1
        
        return l
    
    L = combineSortedArrays(l1, l2)
    # print(L, len(L))
    if len(L) % 2 == 1:
        # odd length array, median is middle
        return L[len(L) // 2]
    else:
        return (L[len(L) // 2] + L[(len(L) // 2) - 1]) / 2
    

def findMedianSortedArraysOptimal(l1, l2):
    # approach - there is actually a way to do this in O(log(n + m)) time 
    # a typical binary search on a sorted array is O(log n) time
    # we can do something similar to a binary search here to find the media
    # eg: [4, 4, 4, 5, 10], [3, 6, 8, 10] take these two arrays
    # now partition them like so
    # [4, 4, 4, | 5, 10] => [4, 4, 4], [5, 10]
    # [3, | 6, 8, 10]    => [3],       [6, 8, 10]
    # => logically same split to get sorted [3, 4, 4, 4, 5, 6, 8, 10, 10] 
    # now every element on the left partitions smaller than every element in the right partitions
    # then we just need to take the smallest element of the right partition and the largest of the left partition
    # and the median will be one of those or the average of both of those

    # whats the approach for finding the partitions?
    # have two pointers, one at the start of the left array, one at the end of the right array
    # make sure the left array is the smaller one
    if len(l1) > len(l2):
        return findMedianSortedArraysOptimal(l2, l1)
    
    # partitions initially set at middle of left and right arrays
    len1, len2 = len(l1), len(l2)
    left = 0
    right = len1

    while left <= right:
        partition1 = (left + right) // 2
        partition2 = (len1 + len2 + 1) // 2 - partition1
        # print(partition1, partition2)
        # When we partition both arrays there are 4 segments total. get max of both left and min of both right
        # [4, 4, 4, | 5, 10] => [4, 4, 4], [5, 10]
        # [3, | 6, 8, 10]    => [3],       [6, 8, 10]
        max_left1 = float('-inf') if partition1 == 0 else l1[partition1 - 1]
        min_right1 = float('inf') if partition1 == len1 else l1[partition1]
        max_left2 = float('-inf') if partition2 == 0 else l2[partition2 - 1]
        min_right2 = float('inf') if partition2 == len2 else l2[partition2]

        # now that we have set our partitions and found our max left and min right values
        # execute the binary search
        if max_left1 <= min_right2 and max_left2 <= min_right1:
            # condition for max_left1 < max_left2 and min_right1 and min_right2 are always true because the arrays
            # are already pre sorted
            # if we have an even length total array then median is average, else middle element
            if (len1 + len2) % 2 == 0:
                return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
            else:
                return max(max_left1, max_left2)
        
        # expand or contract left / right pointers based on max_left1 and min_right2, adjusts partition locations
        elif max_left1 > min_right2:
            right = partition1 - 1
        else:
            left = partition1 + 1


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


# X, Y = generateTestArray()
X, Y = [3, 6], [5, 9, 10]
print(X, Y)
# print(findMedianSortedArrays(X, Y))
print(findMedianSortedArraysOptimal(X, Y))

