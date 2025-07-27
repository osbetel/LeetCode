

"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
"""
def isPalindrome(s: str) -> bool:
    # only consider lowercase and ignore special characters
    # approach - can make something recursive that puts two pointers at the outer edges and moves towards the middle
    # base case is single character for odd palindromes or empty string for even characters
    alphabet_str = "abcdefghijklmnopqrstuvwxyz0123456789"
    alphabet = set(alphabet_str)

    def recurse(left, right):
        # print(left, right, s[left : right + 1], len(s[left : right + 1]))
        if len(s[left : right + 1]) in {0, 1}:
            return True
        
        lchar = s[left].lower()
        rchar = s[right].lower()

        # handle special characters by shifting pointer to ignore
        if lchar not in alphabet:
            return recurse(left + 1, right)

        if rchar not in alphabet:
            return recurse(left, right - 1)
        
        if lchar == rchar:
            return recurse(left + 1, right - 1)
        else:
            return False

    left = 0
    right = len(s) - 1
    return recurse(left, right)


test_cases = [
    "A man, a plan, a canal: Panama", # true
    "race a car", # false
    " ",
    ""
    "0P",
    "aa"
]
for t in test_cases:
    print(isPalindrome(t))