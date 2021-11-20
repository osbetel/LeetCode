# Given a collection of intervals, merge all overlapping intervals.
#
# Example 1:
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:
# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considerred overlapping.

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


def merge(intervals: [[int]]):
    # sort the list by the first index of each interval
    # Then th input:
    # [[1, 9], [2, 5], [19, 20], [10, 11], [12, 20], [0, 3], [0, 1], [0, 2]]
    # Turns into this:
    # [[0, 3], [0, 1], [0, 2], [1, 9], [2, 5], [10, 11], [12, 20], [19, 20]]
    # Then all we need to do is iterate through the intervals and see if the current one
    # contains the first values of the next one.
    # ie: if [0, 3] contains [0,1], [0,2], [1,9], which it does since it contains
    # 1, 2, 1, then the new stitched together interval is [0, 9]
    # since it doesn't contain 10 though, then we start a new interval.
    result = []
    intervals.sort(key = lambda x: x[0])
    # print(intervals)

    for it in intervals:
        if not result or result[-1][1] < it[0]:
            result.append(it)

        else:
            result[-1][1] = max(result[-1][1], it[1])

    return result



i = [[1,3],[2,6],[7,10],[15,18]]
j = [[1,9],[2,5],[19,20],[10,11],[12,20],[0,3],[0,1],[0,2]]
k = [[1, 6], [7, 10], [15, 18]]
print(merge(j))