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
        self.stored = set(array) if array else set()

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