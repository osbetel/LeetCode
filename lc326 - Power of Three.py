# Given an integer, write a function to determine if it is a power of three.
# Example 1:
# Input: 27
# Output: true
#
# Example 2:
# Input: 0
# Output: false
#
# Example 3:
# Input: 9
# Output: true
#
# Example 4:
# Input: 45
# Output: false
# Follow up:
# Could you do it without using any loop / recursion?

def isPowerOfThree(n):
    if n == 1: return True
    if n <= 0: return False
    else: return 4052555153018976267 % n == 0
    # 3^40 = 4052555153018976267 less than word size barely

print(isPowerOfThree(1/3))


# r = []
# for i in range(10000):
#     if isPowerOfThree(i):
#         r.append(i)
# print(r)

# import sys
# for k in range(100):
#     if 3 ** k >= sys.maxsize:
#         print(3**(k-1))
#         print(k)
#         break
