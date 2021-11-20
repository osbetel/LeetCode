# Given a non-empty array of digits representing a
# non-negative integer, plus one to the integer.
#
# The digits are stored such that the most significant
# digit is at the head of the list, and each element in
# the array contain a single digit.
#
# You may assume the integer does not contain any leading
# zero, except the number 0 itself.
#
# Example 1:
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
#
# Example 2:
#
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.

def plusOne(digits):
    # input array is non-empty
    # solution to this is to traverse the array from back to front
    k = str(int("".join(list(str(x) for x in digits))) + 1)
    r = []
    for c in k:
        r.append(int(c))
    return r

print(plusOne([9,9,9,1,2,1,5,1,5,6,8,5,4,3,5,7]))


