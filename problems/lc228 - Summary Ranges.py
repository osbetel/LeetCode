# Given a sorted integer array without duplicates, return the summary of its ranges.
#
# Example 1:
# Input:  [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
#
# Example 2:
# Input:  [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.

def summaryRanges(nums):
    ranges = []
    currRange = []
    for n in nums:
        if n-1 not in currRange:
            currRange = []
            ranges.append(currRange)
        currRange.append(n)

    summary = []
    for x in ranges:
        if len(x) == 1:
            summary.append(str(x[0]))
        else:
            summary.append(str(x[0]) + "->" + str(x[len(x) - 1]))

    return summary


t1 = [0,1,2,4,5,7]
print(summaryRanges(t1))