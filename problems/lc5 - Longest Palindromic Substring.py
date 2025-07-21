

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
    longest = ""
    if len(s) % 2 == 1:
        # handle odd length strings, start at middle, expand outward
        for i in range(len(s)):
            # for each character position, expand outwards while characters match
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # left >= 0 and right < len(s): we start at 0, 0 and remain within bounds of the string
                # s[left] == s[right]: a palindrome should have the same character from center emanating outward
                current_palindrome = s[left:right + 1]
                if len(current_palindrome) > len(longest):
                    longest = current_palindrome
                left -= 1
                right += 1
    else:
        # handle even length strings, there is no middle character
        # but the middle of an even length palindrome should be two of the same character, eg cbba or bbaab
        for i in range(len(s)):
            # for each character position, expand outwards while characters match
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # left >= 0 and right < len(s): we start at 0, 0 and remain within bounds of the string
                # s[left] == s[right]: a palindrome should have the same character from center emanating outward
                current_palindrome = s[left:right + 1]
                if len(current_palindrome) > len(longest):
                    longest = current_palindrome
                left -= 1
                right += 1

    return longest


test = [
    # "babad",     # Expected: "bab" or "aba" 
    "cbbd",      # Expected: "bb"
    "racecar",   # Expected: "racecar"
    "abcdef",    # Expected: "a" (any single char)
    "aabbaa",    # Expected: "aabbaa"
    "abacabad",  # Expected: "abacaba"
    "a",         # Expected: "a"
    ""           # Expected: ""
]
expected = ["bab", "bb", "racecar", "a", "aabbaa", "abacaba", "a", ""]
for t in test:
    print(longestPalindrome(t))
    break



