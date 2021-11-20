# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.
#
# Example 1:
# Input: "()"
# Output: true
#
# Example 2:        Example 5:
# Input: "()[]{}"   Input: "{[]}"
# Output: true      Output: true
#
# Example 3:        Example 4:
# Input: "(]"       Input: "([)]"
# Output: false     Output: false

class Stack:

    def __init__(self):
        self.stack = []

    def add(self, dataval):
        # Use list append method to add element
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False

    # Use peek to look at the top of the stack

    def peek(self):
        return self.stack[0]


def isValid(s):
    if len(s) % 2 != 0: return False
    # if s == "()" or s == "{}" or s == "[]" or s == "": return True
    else:
        stack = []
        for p in s:
            if isClosingBracket(p):
                if stack == []: return False
                if isMatchingPair(stack[len(stack) - 1], p):
                    stack.pop(len(stack) - 1)
            else:
                stack.append(p)

    return stack == []


def isClosingBracket(a):
    if a == ")" or a == "}" or a == "]": return True
    else: return False


def isMatchingPair(a, b):
    if a == "(" and b == ")": return True
    if a == "{" and b == "}": return True
    if a == "[" and b == "]": return True
    return False


print(isValid("()"))        # True
print(isValid("()[]{}"))    # True
print(isValid("(]"))        # False
print(isValid("([)]"))      # False
print(isValid("{[]}"))      # True
print(isValid("(()("))      # False
print(isValid("){"))        # False

