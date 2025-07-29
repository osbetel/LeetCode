"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such 
that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
"""

def minWindowOptimal(s: str, t: str) -> str:
    # Optimal sliding window approach with hashmap
    if not s or not t or len(s) < len(t):
        return ""
    
    # Count characters in t
    t_count = {}
    for char in t:
        t_count[char] = t_count.get(char, 0) + 1
    
    # Sliding window variables
    left = 0
    min_len = float('inf')
    min_start = 0
    required = len(t_count)  # Number of unique chars in t
    formed = 0  # Number of unique chars in current window with desired frequency
    window_count = {}
    
    for right in range(len(s)):
        # Expand window by including s[right]
        char = s[right]
        window_count[char] = window_count.get(char, 0) + 1
        
        # Check if frequency of current char matches desired count in t
        if char in t_count and window_count[char] == t_count[char]:
            formed += 1
        
        # Contract window until it's no longer valid
        while left <= right and formed == required:
            char = s[left]
            
            # Update minimum window if current is smaller
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_start = left
            
            # Remove leftmost character from window
            window_count[char] -= 1
            if char in t_count and window_count[char] < t_count[char]:
                formed -= 1
            
            left += 1
    
    return "" if min_len == float('inf') else s[min_start:min_start + min_len]


def minWindowNaive(s, t):
    # naive approach - we can generate every substring and check all of them
    # to generate every possible substring
    # need to generate all of size 1, 2, ..., len(s)
    # inner for loop goes through all strings of size 1, then 2, up to len(s) + 1
    # for a string "abcd", it has
    # 1 substr of size 4
    # 2 substr of size 3
    # 3 substr of size 2
    # 4 substr of size 1
    # so if n is length of string, the formula is n(n + 1) / 2 => O(n^2) time complexity
    # space complexity is the same to store the same amount of substrs

    def getAllSubstrs(s):
        substrs = []
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                sub = s[i : j + 1]
                # print(i, j, sub)
                substrs.append(sub)
        return substrs
    
    # then for every substring, if it containes all target characters then store smallest
    res = set()
    substrs = getAllSubstrs(s)
    smallest = "*" * 1000
    for sub in substrs:
        if all([x in set(sub) for x in t]):
            res.add(sub)
            smallest = sub if len(sub) < len(smallest) else smallest
    return smallest


def minWindow(s: str, t: str) -> str:
    # what's the optimal approach instead? 
    # perhaps we can use some kind of expanding and contracting window?
    # approach - start with a small window of size 1 at the front of the array
    # expand the right side and keep track of characters and their countswith a hashmap
    # when the condition is true for all characters in target being in the substr,
    # save that size, contract the left pointer until condition is no longer true, then iterate again

    left, right = 0, 0
    chars_in_window = {}
    smallest = ""

    # this is O(n^2) actually, we iterate through, and each count() also iterates through
    # use a for loop for O(n) time
    # target_chars = {k: t.count(k) for k in t}
    target_chars = {}
    for c in t:
        target_chars[c] = target_chars.get(c, 0) + 1

    required = len(target_chars)
    found = 0

    while right < len(s):
        # expand window to the right
        char = s[right]
        chars_in_window[char] = chars_in_window.get(char, 0) + 1
        
        # check character frequency matches
        if char in target_chars and chars_in_window[char] == target_chars[char]:
            found += 1
        
        # contract from the left
        while left <= right and found == required:
            substr = s[left:right+1]
            # save smallest and remove left character and increment left pointer
            smallest = substr if len(substr) < len(smallest) or smallest == "" else smallest
            
            # remove leftmost character from window
            left_char = s[left]
            chars_in_window[left_char] = chars_in_window.get(left_char, 0) - 1
            if left_char in target_chars and chars_in_window[left_char] < target_chars[left_char]:
                found -= 1
            left += 1
        
        right += 1

    return smallest
        


tests = [
    ("ADOBECODEBANC", "ABC"),
    ("a", "a"),
    ("a", "aa")
]

for t in tests:
    b = print(minWindowOptimal(*t))
