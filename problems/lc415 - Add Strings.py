# Given two non-negative integers num1 and num2 represented
# as string, return the sum of num1 and num2.
#
# Note:
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

def addStrings(num1, num2):
    return str(eval(num1) + eval(num2))


print(addStrings("123","321"))



