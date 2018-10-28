# Given a string, find the length of the longest substring without repeating characters.
#
# Example 1:
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", which the length is 3.
#
# Example 2:
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
# Example 3:
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


def lengthOfLongestSubstring(s):
    count = 0
    longest = 0
    seen = set()
    mostRecentChar = ""

    for c in s:
        if c not in seen:
            loop = "first"
            count += 1
            longest = max(count, longest)
            seen.add(c)
            mostRecentChar = c

        elif c in seen:
            loop = "second"
            if c == mostRecentChar:
                seen = set(c)
                count = 1
            elif c != mostRecentChar:
                seen = {mostRecentChar,c}
                count = len(seen)

        # print(seen, count, loop, c, mostRecentChar)

    return longest


print(lengthOfLongestSubstring("abcabcbb")) # 3
print(lengthOfLongestSubstring("bbbbb"))    # 1
print(lengthOfLongestSubstring("pwwkew"))   # 3
print(lengthOfLongestSubstring("aab"))      # 2
print(lengthOfLongestSubstring("dvdf"))     # 3
print(lengthOfLongestSubstring("anviaj")) # 5


