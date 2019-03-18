

# Input is a string n, which is an integer. Goal is to return the amount of operations it takes to get from n to 1.
# The three possible operations are as follows:
#   1) add one
#   2) Subtract one
#   3) divide by 2 (only possible for even numbers)
#
# Clearly, the easiest way is to already have an input that is a power of 2. ie: 2, 4, 8, 16, 32, 64, etc.
# So the goal should be to get to a power of 2. We need to write a function that will check if something is a power of 2.
#
# Easiest way to do that is to have a global variable defined as a list of all powers of 2 that are less than the integer
# constraint, which is 309 digits long. So 99999...999 Until it's 309 digits long. Or 1 * 10^309 - 1 as an upper limit

def answer(n):
    x = int(n)
    steps = 0

    while x != 1:
        if x % 2 == 0:
            x /= 2
            steps += 1
        else:
            if ((x + 1) / 2) % 2 == 0 and (x != 3):
                x += 1
            else:
                x -= 1
            steps += 1
    return steps