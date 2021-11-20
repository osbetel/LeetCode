
# Given a string containing digits from 2-9 inclusive, return
# all possible letter combinations that the number could represent.
# A mapping of digit to letters (just like on the telephone buttons)
# is given below. Note that 1 does not map to any letters.
# Example:
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

def letterCombinations(digits):

    values = {"2": ["a", "b", "c"],
              "3": ["d", "e", "f"],
              "4": ["g", "h", "i"],
              "5": ["j", "k", "l"],
              "6": ["m", "n", "o"],
              "7": ["p", "q", "r", "s"],
              "8": ["t", "u", "v"],
              "9": ["w", "x", "y", "z"]
              }

    # given "234..." we want to set up a recursive function that does
    # for each value of 2, add on each value of 3,
    # for each value of 3, add on each value of 4... So on.

    letters = []
    for n in range(0, len(digits)):
        num = digits[n]
        if values.__contains__(num):
            addChars = values.get(str(num))
            letters = combination(letters, addChars)

        # [x * y for x, y in product(A, B)]

    return letters


def combination(set1, set2):

    if set1 == []:
        return set2

    # set1plus2 = list(itertools.product(set1, set2))
    set1plus2 = []

    for x in set1:
        for y in set2:
            set1plus2.append(x + y)

    return set1plus2


k = letterCombinations("3523")
print(k)





