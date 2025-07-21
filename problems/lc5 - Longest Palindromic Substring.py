

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

class Solution:
    cache = set()
    longest = ""

    def longestPalindrome(self, s: str) -> str:
        self.recurse(s)
        r = self.longest
        self.cache.clear()
        self.longest = ""
        return r

    def recurse(self, s: str) -> str:
        k = [s, s[:-1],s[1:]]
        for sub in k:
            if sub in self.cache:
                continue
            elif sub == "":
                continue
            else:
                self.cache.add(sub)
                l = len(sub)
                if self.is_palindrome(sub):
                    if l > len(self.longest):
                        self.longest = sub
        a, b = "", ""
        if s[:-1] != "":
            a = self.recurse(s[:-1])
        if s[1:] != "":
            b = self.recurse(s[1:])
        return max(self.longest, a, b)

    def is_palindrome(self, s, count=0):
        if len(s) <= 1:
            return True
        if s[0] == s[-1]:
            return self.is_palindrome(s[1:-1], count+2)
        return False


def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    return False

longest = ""

def longest_palindrome(s):
    global longest
    # a new approach required because the above with memoization is not suitable
    # once again we approach with the top down approach -> S is a palindrome iff S[1:-1] is also a palindrome
    # one change we can make though is that instead of caching all the recursive subproblems, we need to
    # avoid those recursive branches entirely
    if is_palindrome(s):
        if len(longest) < len(s):
            longest = s
    if s[1:] != "":
        longest_palindrome(s[1:])
    if s[:-1] != "":
        longest_palindrome(s[:-1])
    return longest

def longestPalindrome1(s: str) -> str:

    n = len(s)
    # Form a bottom-up dp 2d array
    # dp[i][j] will be 'true' if the string from index i to j is a palindrome.
    dp = [[False] * n for _ in range(n)]

    ans = ''
    # every string with one character is a palindrome
    for i in range(n):
        dp[i][i] = True
        ans = s[i]

    maxLen = 1
    for start in range(n - 1, -1, -1):
        for end in range(start + 1, n):
            # palindrome condition
            if s[start] == s[end]:
                # if it's a two char. string or if the remaining string is a palindrome too
                if end - start == 1 or dp[start + 1][end - 1]:
                    dp[start][end] = True
                    if maxLen < end - start + 1:
                        maxLen = end - start + 1
                        ans = s[start: end + 1]
    return ans


import time

test = ["abba"]
expected = [""]

for a, b in zip(test, expected):
    now = time.time_ns()
    k = longest_palindrome(a)
    longest = ""
    later = time.time_ns()
    print(later - now, k, b, "current")

    now = time.time_ns()
    s = Solution()
    k = s.longestPalindrome(a)
    later = time.time_ns()
    print(later - now, k, b, "prior")

    now = time.time_ns()
    k = longestPalindrome1(a)
    later = time.time_ns()
    print(later - now, k, b, "new")



