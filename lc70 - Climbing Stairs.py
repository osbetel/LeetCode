# See lc746 for a similar problem
# Given a staircase with n steps, if you can step up one step
# or two steps at a time, how many distinct ways can you climb to the top?
#
# So if we have a staircase of 2 steps, we can do 1 step + 1 step, or 2 steps, making
# 2 distinct ways we can get to the top.
#
# With 3 steps, this becomes
# 1 + 1 + 1
# 1 + 2
# 2 + 1
# 3 total
#
# And with 4 steps
# 1 + 1 + 1 + 1
# 1 + 2 + 1
# 1 + 1 + 2
# 2 + 1 + 1
# 2 + 2
# 5 total
#
# and with 5 steps...
# 1 + 1 + 1 + 1 + 1
# 1 + 1 + 1 + 2
# 1 + 1 + 2 + 1
# 1 + 2 + 1 + 1
# 2 + 1 + 1 + 1
# 1 + 2 + 2
# 2 + 1 + 2
# 2 + 2 + 1
# Or 8 total
#
# so already we can see that there is a pattern, and the pattern is a combinatorics problem.
#
# Taking 5 steps as an example, we can get the number of distinct ways by
# nCr(5,0) + nCr(4, 1) + nCr(3,2)
# or 1 + 4 + 3 = 8 distinct ways to climb a staircase of 5 steps.
# For some nCr(n,r), we're asking how many ways can we arrange n elements, if we must choose r?

def factorial(x):
    import math
    return math.factorial(x)

def nCr(n, r):
    # nCr(n, r) = n! / r! (n - r)!
    return int(factorial(n) / (factorial(r) * factorial(n - r)))

def waysToClimbNStairs(x: int) -> int:
    ways = 0
    for n in reversed(range(1, x + 1)):
        r = x - n
        if n < r:
            return ways
        ways += nCr(n,r)

    return int(ways)

# We should also note the dynamic programming solution.
# In order to get to some step s[i], you can either jump one step from s[i - 1] or two steps from s[i - 2]
# So the number of ways to get to s[i] is equal to s[i - 1] + s[i - 2}

def waysToClimbNStairsDynamicProg(x):
    if x == 2:
        return 2
    else:
        return waysToClimbNStairsDynamicProg(x - 1) + waysToClimbNStairs(x - 2)

x = 5
print(waysToClimbNStairs(x))
print(waysToClimbNStairsDynamicProg(x))

# We can also note that the sequence of ways to climb is the fibonacci sequence.
# 0 steps ==> 1 way to climb
# 1 step  ==> 1 way
# 2 steps ==> 2 ways
# 3 steps ==> 3 ways
# 4 steps ==> 5 ways
# 5 steps ==> 8 ways
# 6 steps ==> 13 ways
# ... etc. So to find the num of ways for a staircase of length n,
# we simply need to find the nth fibonacci number


