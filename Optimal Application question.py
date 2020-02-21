# Andrew Nguyen, – Optimal online application, hire me pls
# I'm going to treat this like a typical coding interview and run through all the cases.
# first, some constraints, the question is asking for the sum of all numbers less than 1000,
# that are multiples of 3 or 5, NOT including 1000. Stricly less than.

def sum_less_than_onek():
    # this is the most basic, naive case. it's exactly θ(n) time(exactly 1000 comparisons), but we can do better.
    s = 0
    for i in range(0,1000):
        if (i % 3 == 0) or (i % 5 == 0):
            s += i

    return s


def sum_less_than_onek2():
    # since it's specifically multiples of 3 and 5, we can actually just iterate up by 3s and 5s, ignoring the
    # numbers in between. 999 // 3 == 333, and 999 // 5 == 199, so really we only need to hit 532
    # digits instead of all 1000.
    s = 0

    for i in range(0, 1000, 3): # 0, 3, 6,...
        s += i

    for i in range(0, 1000, 5): #0, 5, 10, 15,...
        s += i

    for i in range(0, 1000, 15): # multiples of both 3 and 5 are counted twice, so we must subtract one of each
        s -= i                   # 0, 15, 30,...

    return s


def sum_less_than_k(k, a, b):
    # Have we heard of summations? Math is cool.
    # the sum of a sequence, 1, 2, 3,..., n = (n(n + 1)) / 2, lets call this f(n)
    # additionally we know that the number of terms divisible by 3 is 999//3 == 333, and by 5 is 999//5 == 199
    # and 999//15 == 66. So we can use 3 * f(999//33) for the sum of all multiples of 3 under 1000
    # and likewise for the rest of them.
    # This is a true constant time solution for any positive integer k, and multiples a and b.
    def f(n):
        return (n * (n + 1)) / 2

    s = 0
    s += a * f((k - 1) // a)
    s += b * f((k - 1) // b)
    s -= (a * b) * f((k - 1) // (a * b))

    return s


print(sum_less_than_k(1000, 3, 5))
