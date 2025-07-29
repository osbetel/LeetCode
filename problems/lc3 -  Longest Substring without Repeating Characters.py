"""Given a string, find the length of the longest substring without repeating characters.

Example 1:
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", which the length is 3.

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

def lengthOfLongestSubstring(s: str) -> int:
    # approach - use two pointers in a single for loop
    # expand right side until we run into a character we have seen before
    # when that happens, contract the left side until that condition is no longer true
    # do until end of string
    left = 0
    seen_chars = set()
    longest_len = 0
    longest_str = ""
    for right in range(len(s)):
        # print(left, right, s[left:right], longest_str, longest_len)
        while s[right] in seen_chars:
            seen_chars.remove(s[left])
            left += 1
        seen_chars.add(s[right])
        longest_str = s[left : right + 1] if len(s[left : right + 1]) > longest_len else longest_str
        longest_len = len(longest_str)
    return longest_str, longest_len


a = [
    "abcabcbb",
    "bbbbb",
    "pwwke",
    "pwwkew"
]
for x in a:
    print(lengthOfLongestSubstring(x))