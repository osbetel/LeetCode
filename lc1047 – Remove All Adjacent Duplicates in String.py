# Given a string S of lowercase letters, a duplicate removal consists of choosing
# two adjacent and equal letters, and removing them.
# We repeatedly make duplicate removals on S until we no longer can.
# Return the final string after all such duplicate removals have been made.
# It is guaranteed the answer is unique.
#
# Input: "abbaca"
# Output: "ca"
# Explanation:
# For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal,
# and this is the only possible move. The result of this move is that the string is "aaca",
# of which only "aa" is possible, so the final string is "ca".

def removeDuplicates(s: str) -> str:
    """
    Approach: Notice that any even length palindrom sequence is able to be removed
    eg: "abbaabba" can be removed in its entirety as we can remove the center "aa" getting "abbbba"
    followed by removing "bbbb" to get "aa" and then removing "aa" entirely.

    so how do we find even length palindromes?
    """


def removeDuplicates(s: str) -> str:
    import re
    regex = re.compile(r'(.)\1')
    # print(s)
    while len(s) > 1 and regex.search(s):
        s = regex.sub('', s)
        # print(s)
    return s

print(removeDuplicates("aaabbbabbababbabbbaaaaa"))