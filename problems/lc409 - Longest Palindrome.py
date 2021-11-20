# Given a string which consists of lowercase or uppercase letters,
# find the length of the longest palindromes that can be built with those letters.
#
# This is case sensitive, for example "Aa" is not considered a palindrome here.
#
# Note:
# Assume the length of given string will not exceed 1,010.
#
# Example:
# Input:
# "abccccdd"
#
# Output:
# 7
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.

def longestPalindrome(s):
    # An easy and straight forward way to do this is to count the number of
    # pairs in the string, and then add 1 if there exists a single letter anywhere

    pairs = {}
    for ch in s:
        addOne(ch, pairs)

    if len(pairs) == 1:
        return pairs.get(s[0])

    longest = 0
    for p in pairs:
        longest += (pairs.get(p) // 2 * 2)
        if longest % 2 == 0 and pairs.get(p) % 2 == 1:
            longest += 1

    return longest


def addOne(x, pairs):
    if x not in pairs:
        pairs.update({x: 1})
    else:
        pairs.update({x: pairs.get(x) + 1})

print(longestPalindrome("aaa"))         # 3
print(longestPalindrome("ccccccc"))     # 7
print(longestPalindrome("abccccdd"))    # 7
print(longestPalindrome("bb"))          # 2

