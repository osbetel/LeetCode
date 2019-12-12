
# You're given strings J representing the types of stones that are jewels,
# and S representing the stones you have.  Each character in S is a type
# of stone you have.  You want to know how many of the stones you have are also jewels.
#
# The letters in J are guaranteed distinct, and all characters in J and
# S are letters. Letters are case sensitive, so "a" is considered a
# different type of stone from "A".
#
# Example 1:
#
# Input: J = "aA", S = "aAAbbbb"
# Output: 3
# Example 2:
#
# Input: J = "z", S = "ZZ"
# Output: 0
# Note:
#
# S and J will consist of letters and have length at most 50.
# The characters in J are distinct.

def numJewelsInStones(J: str, S: str):
    """
    For each character in S that is also in J, +1 to total # of jewels
    """

    if J == "" or S == "":
        return 0

    total = 0
    for ch in S:
        if ch in J: total += 1
    return total


print(numJewelsInStones("aA", "aAAbbbb"))








