# Write a function that takes a string as input and reverse only the vowels of a string.
#
# Example 1:
#
# Input: "hello"
# Output: "holle"
# Example 2:
#
# Input: "leetcode"
# Output: "leotcede"
# Note:
# The vowels does not include the letter "y".

def reverseVowels(s):
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    string = list(s)
    vInStr = []

    for v in string:
        if v in vowels:
            vInStr.append(v)


    for i in range(len(string)):
        if string[i] in vowels:
            string[i] = vInStr.pop()

    return "".join(string)

print(reverseVowels("aA"))


