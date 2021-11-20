
# given some array N, of costs to climb steps,
# and given that you can only climb one or two steps (jumps) at a time,
# what is the min cost to get to the top?
#
# eg: N = [10, 15, 20]
# You could do 1 step, 3 times, for a cost of 10 + 15 + 20
# or step to 10, then 15, then to the top for a cost of 10 + 15
# or just jump two steps to 15, then two more to the top which is 15 in cost.
# That's the optimal one, but how can you do this for any problem?
#
# N is between 2 and 1000 elements long,
# any n in N is 0 to 999.

# This is a dynamic programming problem. The naive approach involves generating
# a set of all legitimate jumps to the top, ie: from the example above,
# 10,15,20 or 10,20 or 15,20 or 15... and then taking the one with the lowest cost.
#
# Alternatively, we can start from the top and step down, and take advantage of
# optimal substructure characteristic of DP problems.
#
# ie: start at the top, you can step down to 20 (1 step) or 15 (2 steps),
# choose the one which is cheaper

def minCostClimbingStairs(cost: [int]) -> int:
    # ok so the greedy solution doesn't work because in the case
    # of N = [0,2,2,1], starting from the right, we choose to step to 1.
    # When really we should jump to 2, and then to 0
    right = 0
    left = 0
    for x in reversed(range(len(cost))):
        prevLeft = right
        right = cost[x] + min(right,left)
        left = prevLeft
    print(min(right,left))
    return min(right,left)

a = [10,15,20]
b = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
c = [1,2,4,4,5,2,5,23,5,5,23,4,2,34,2,35,6,5,47,4567,5,67,3]
d = [0,2,2,1]
minCostClimbingStairs(c)



