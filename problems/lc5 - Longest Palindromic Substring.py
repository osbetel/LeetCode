

# given a string s, return the longest palindromic substring in s
# a few notes:
# first a palindrome is a string that is read the same forward as it is backwards
# the characters can be non-unique as well, ie: "bbb" is a palindrome just as "aba" is

# import random
# b = ''.join(random.choices(["a", "b", "c"], k=10))

#     # in dynamic programming we have typically two concepts.
#     # the first is memoization. suppose we're making a recursive call to a function that gives us the
#     # fibonacci sequence. fib(10) = fib(9) + fib(8), fib(9) = fib(8) + fib(7), ... etc
#     # notice how fib(8) appears twice? We can cache this result in a map so that
#     # we don't have to recalculate it again should it appear in the tree of subproblems
#     # this is also known as "top down"
#     #
#     # so here, consider a string S of length n
#     # S is a palindrome if S[0] == S[n - 1], AND if S[1, n - 1 - 1] is a palindrome

def longestPalindrome(s):
    # not the optimal solution but we will implement a expand around the center style solution
    #   def expand_around_center(s, left, right):
    #     while left >= 0 and right < len(s) and s[left] == s[right]:
    #         left -= 1
    #         right += 1
    #     return right - left - 1  # length of palindrome
    longest = s[0] if s else ""
    for i in range(len(s)):
        # for each character, expand left and right until palindorme invalid
        # then record length
        left, right = i, i
        while 0 <= left and right < len(s):
            if s[left] != s[right]:
                break
            current_string = s[left : right + 1]
            if len(current_string) > len(longest):
                longest = current_string
            left -= 1
            right += 1

        left, right = i, i + 1
        while 0 <= left and right < len(s):
            if s[left] != s[right]:
                break
            current_string = s[left : right + 1]
            if len(current_string) > len(longest):
                longest = current_string
            left -= 1
            right += 1

    return longest


test = [
    "babad",     # Expected: "bab" or "aba" 
    "cbbd",      # Expected: "bb"
    "racecar",   # Expected: "racecar"
    "abcdef",    # Expected: "a" (any single char)
    "aabbaa",    # Expected: "aabbaa"
    "abacabad",  # Expected: "abacaba"
    "abb",         # Expected: "a"
    ""           # Expected: ""
]
expected = ["bab", "bb", "racecar", "a", "aabbaa", "abacaba", "bb", ""]
for t in test:
    print(longestPalindrome(t))



