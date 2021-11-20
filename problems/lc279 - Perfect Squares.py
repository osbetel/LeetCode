# Given a positive integer n, find the least number of perfect
# square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
#
# Example 1:
# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
#
# Example 2:
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.


def numSquares(n):
    # by Langrange's four-square theorem, we know that any natural number n in N
    # can be represented as the sum of 4 integer squares
    # eg: 3 = 1^2 + 1^2 + 1^2 + 0^2
    #    31 = 5^2 + 2^2 + 1^2 + 1^2
    #   310 = 17^2 + 4^2 + 2^2 + 1^2
    # This theorem implies that any natural number n can be expressed as a sum of
    # 4 perfect squares at most. So numSquares should never return more than 4 or less than 1
    # loops checking the sum of squares
    #
    # Thus some integer n is written as n = a^2 + b^2 + c^2 + d^2
    # Note that there are multiple ways this can be done, and we really just want the smallest possible
    # number of ways
    # So for example 123 = 11^2 + 1^2 + 1^2, and 123 = 7^2 + 7^2 + 5^2
    a = 0
    while a ** 2 <= n:
        b = a
        while b ** 2 <= n:
            c = b
            while c ** 2 <= n:
                d = c
                while d ** 2 <= n:

                    # if sum of four squares equals
                    # the given no.
                    if (a ** 2 + b ** 2 + c ** 2 + d ** 2) == n:
                        return int(a != 0) + int(b != 0) + int(c!= 0) + int(d != 0)
                        # printing the numbers
                        # print("{} = {}*{} + {}*{} +".
                        #       format(n, a, a, b, b), end=" ")
                        # print("{}*{} + {}*{}".
                        #       format(c, c, d, d), end="\n")
                    d += 1
                c += 1
            b += 1
        a += 1

    return

print(numSquares(4))




