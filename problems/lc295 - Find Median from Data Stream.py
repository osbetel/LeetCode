"""
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:
Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
"""

import bisect
import heapq
class MedianFinder:

    # how can we keep track of the median of a stream?
    # we could use a data structure that keeps elements in sorted order, and then simply access the middle element(s) 
    # something like a binary search tree works, but may be overkill here. An array where we do a sorted insert
    # with something like a binary search allows for O(log n) insert (and O(n) to shift array, so O(n) inserts really)
    # while accessing middle elements is O(1)

    # def __init__(self, array=[]):
    #     self.values = []
    #     for x in array:
    #         self.addNum(x)

    # def addNum(self, x: int) -> None:
    #     bisect.insort(self.values, x)

    # def findMedian(self) -> float:
    #     L = len(self.values)
    #     if L % 2 == 1:
    #         return self.values[L // 2]
    #     else:
    #         return (self.values[L // 2] + self.values[(L // 2) - 1]) / 2

    # alternatively we can use a min-heap and a max-heap. 
    # with a heap the inserted values are balanced between the left and right tree leaves (it's a binary tree underneath)
    # in doing this we can keep track of the middle two elements, see the example below
    #   3              4
    #  / \            / \
    # 2   1          5   6

    def __init__(self, array=[]):
        self.min_heap = []
        self.max_heap = []
        for x in array:
            self.addNum(x)

    def addNum(self, x):
        # algorithm - if both heaps are empty, add to one of the heaps
        # if only one heap is empty, add to the other and rebalance if needed
        # otherwise need to compare x to the tops of both heaps and put it in the one it belongs
        if not self.min_heap or x >= self.min_heap[0]:
            heapq.heappush(self.min_heap, x)
        else:
            heapq.heappush(self.max_heap, -x) # heapq is a min heap implementation. Negate the values w/ -1 for a logical max heap

        # if the heap sizes have a size difference greater than 1, find the bigger one, pop it's top value, add to other heap
        if len(self.min_heap) > len(self.max_heap) + 1:
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        elif len(self.min_heap) + 1 < len(self.max_heap):
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        
        print(self.min_heap, [-x for x in self.max_heap])

    def findMedian(self):
        minL, maxL = len(self.min_heap), len(self.max_heap)
        totalL = minL + maxL
        if totalL % 2 == 1:
            return self.min_heap[0] if minL > maxL else -self.max_heap[0]
        else:
            return (self.min_heap[0] + -self.max_heap[0]) / 2


mf = MedianFinder()
# array = [19, 19, 24, 25, 25, 27, 25, 35, 30, 26, 35, 35, 28, 34, 27, 40, 35, 38, 31, 33, 31, 18, 16, 14, 14, 11, 6, 14, 14, 14, 10, 0, 3, 2, 13, 5, 12, 4, 11, 8, 0]
array = [40, 12, 16]
for x in array:
    mf.addNum(x)
print(mf.findMedian())

