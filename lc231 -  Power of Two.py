# Given an integer, write a function
# to determine if it is a power of two.
#
# Example 1:
# Input: 1
# Output: true
# Explanation: 2^0 = 1
#
# Example 2:
# Input: 16
# Output: true
# Explanation: 2^4 = 16
#
# Example 3:
# Input: 218
# Output: false

def isPowerOfTwo(n):
    if n == 0: return False
    if n == 1: return True

    # uniquely, all powers of 2 when expressed in their bitwise form
    # are comprised of all zeros and a single 1.
    # So we can just return whether or not the sum of all the bits 0, 1 == 1
    return (n & (n-1)) == 0


t = []
for x in range(257):
    if isPowerOfTwo(x):
        t.append(x)
print(t)
