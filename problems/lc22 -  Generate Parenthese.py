# Given n pairs of parentheses, write a function to generate
# all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

def generateParenthesis(n):
    result = []

    def construct(s, left, right):
        if len(s) == 2*n:
            result.append(s)      # if the string is of the proper length
            return
        if left < n:
            construct(s + "(", left + 1, right)
        if right < left:
            construct(s + ")", left, right + 1)

    construct("", 0, 0)
    return result

k = generateParenthesis(3)
print(k)
