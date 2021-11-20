# We are playing the Guess Game. The game is as follows:
#
# I pick a number from 1 to n. You have to guess which number I picked.
#
# Every time you guess wrong, I'll tell you whether the number is higher or lower.
#
# You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):
#
# -1 : My number is lower
#  1 : My number is higher
#  0 : Congrats! You got it!
#
# Example :
# Input: n = 10, pick = 6
# Output: 6

def guess(g, n):
    if g == n:
        return 0
    elif g < n:
        return 1
    else:
        return -1

def guessNumber(n):
    a = 1
    b = n
    g = int((a + b) / 2)
    from random import randint as ri
    r = ri(1, n)

    while a <= b:

        # g = int(a + (b - a) / 2)
        d = guess(g, r)
        # print(a, g, b, d, r)

        if d == 0:
            return g

        elif d == -1:
            b = g
            g = int((a + b) / 2)

        else:
            a = g
            g = int((a + b) / 2) + 1

    return

    # I specify a range 1 -  n
    # a random int is selected, guess the right one!
for x in range(1000000):
    print(guessNumber(500))



