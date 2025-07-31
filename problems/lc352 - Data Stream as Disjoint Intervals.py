"""
Given a data stream input of non-negative integers a1, a2, ..., an, 
summarize the numbers seen so far as a list of disjoint intervals.

Implement the SummaryRanges class:
SummaryRanges() Initializes the object with an empty stream.
void addNum(int value) Adds the integer value to the stream.
int[][] getIntervals() Returns a summary of the integers in the 
stream currently as a list of disjoint intervals [starti, endi]. 
The answer should be sorted by starti.
 

Example 1:
Input
["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
[[], [1], [], [3], [], [7], [], [2], [], [6], []]
Output
[null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7, 7]], null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]

Explanation
SummaryRanges summaryRanges = new SummaryRanges();
summaryRanges.addNum(1);      // arr = [1]
summaryRanges.getIntervals(); // return [[1, 1]]
summaryRanges.addNum(3);      // arr = [1, 3]
summaryRanges.getIntervals(); // return [[1, 1], [3, 3]]
summaryRanges.addNum(7);      // arr = [1, 3, 7]
summaryRanges.getIntervals(); // return [[1, 1], [3, 3], [7, 7]]
summaryRanges.addNum(2);      // arr = [1, 2, 3, 7]
summaryRanges.getIntervals(); // return [[1, 3], [7, 7]]
summaryRanges.addNum(6);      // arr = [1, 2, 3, 6, 7]
summaryRanges.getIntervals(); // return [[1, 3], [6, 7]]
"""
from typing import List
class SummaryRanges:

    def __init__(self, array=[]):
        # Use a set for O(1) insertion and automatic duplicate handling
        # another way we could do it is to have some sorted of data structure that handles
        # sort on insertion so that we can avoid O(n log n) sort on calling getIntervals
        # this could be like a balanced binary search tree... Probably major overkill though for 
        # a leetcode problem in 30 minutes to implement from scratch (python does not have a BST implementation)
        self.stored = set(array) if array else set()

        # here's an implementation that uses bisect library, which is essentially like a BST using binary search on 
        # an iterable to keep inserted elements sorted. insert is O(log n) time, O(n) to shift the array... So really only works for small N
        # import bisect
        # self.stored = [0] * 100
        # bisect.insort_left

        # alternatively can do it with a heap
        # this is O(log n) insert, maintains sorted order when popping from the heap, but 
        # import heapq
        # heap = []
        # heapq.heappush(heap, 5)
        # heapq.heappush(heap, 1)
        # heapq.heappush(heap, 3)
        # heapq.heappop(heap)

        # another alternative is to use a SortedList
        # uses a B+ tree as the underlying data structure
        # insertion and removal is O(log n), so is search and index access
        # iteration of the list still O(n)
        # from sortedcontainers import SortedList
        # sl = SortedList([])
        # sl.add(5)
        # sl.add(1)
        # sl.add(3)

    def addNum(self, value: int) -> None:
        self.stored.add(value)

    def getIntervals(self) -> List[List[int]]:
        # given some array [1,2,3,7,8,10,15] => [[1,3], [7,8], [10, 10] [15, 15]]
        # approach - two pointers, both start at 0,
        # expand right pointer out while continous
        # when not continuous, add [left, right], then move pointers up to current
        if not self.stored:
            return []
        
        # Sort the set only when needed
        sorted_nums = sorted(self.stored)
        
        res = []
        left, right = 0, 0
        while right < len(sorted_nums) - 1:
            if sorted_nums[right] + 1 == sorted_nums[right + 1]:
                right += 1
            else:
                res.append([sorted_nums[left], sorted_nums[right]])
                right += 1
                left = right
        
        # Add the final interval
        res.append([sorted_nums[left], sorted_nums[right]])
        return res
                


    
# Your SummaryRanges object will be instantiated and called as such:
summaryRanges = SummaryRanges(array=[1,2,3,7,8,10,15])
k = summaryRanges.getIntervals()
print(k)


# here's an implementation that uses binary search tree
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class SummaryRanges:
    def __init__(self, array=[]):
        self.root = None
        for x in array:
            self.addNum(x)

    def addNum(self, value: int) -> None:
        self.root = self._insert(self.root, value)

    def _insert(self, node, val):
        if not node:
            return TreeNode(val)
        if val < node.val:
            node.left = self._insert(node.left, val)
        elif val > node.val:  # Ignore duplicates
            node.right = self._insert(node.right, val)
        return node

    def getIntervals(self) -> List[List[int]]:
        # In-order traversal to get sorted values
        values = []
        self._inorder(self.root, values)

        if not values:
            return []

        # Build intervals from sorted values
        intervals = []
        start = values[0]
        end = values[0]

        for i in range(1, len(values)):
            if values[i] == end + 1:
                end = values[i]
            else:
                intervals.append([start, end])
                start = end = values[i]

        intervals.append([start, end])
        return intervals

    def _inorder(self, node, values):
        if node:
            self._inorder(node.left, values)
            values.append(node.val)
            self._inorder(node.right, values)

summaryRanges = SummaryRanges(array=[1,2,3,7,8,10,15])
k = summaryRanges.getIntervals()
print(k)