# Given two strings s and t which consist of only lowercase letters.
#
# String t is generated by random shuffling string s and then add one more letter at a random position.
#
# Find the letter that was added in t.
#
# Example:
# Input:
# s = "abcd"
# t = "abcde"
# Output:
# e
# Explanation:
# 'e' is the letter that was added.

def findTheDifference(s, t):

    for tring in s:
        t = t.replace(tring, "", 1)

    return t

def addToDict(x, d):
    if x not in d:
        d.update({x: 1})
    else:
        d.update({x: d.get(x) + 1})


s = "abcdeabcdebba"
t = "abcdeasbcdebba"
print(findTheDifference(s, t))


