# Input: s = "RLRRLLRLRL"
# Output: 4
# Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
#
# Input: s = "RLLLLRRRLR"
# Output: 3
# Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.
#
# Input: s = "LLLLRRRR"
# Output: 1
# Explanation: s can be split into "LLLLRRRR".

def solution(s: str) -> int:
    a = 0
    b = 0
    touchedIndices = []

    for i in range(len(s) - 1):
        pair = s[i] + s[i+1]
        if pair == "RL" and  i not in touchedIndices:
            a += 1
            touchedIndices.append(i)
            touchedIndices.append(i+1)
        elif pair == "LR" and  i not in touchedIndices:
            b += 1
            touchedIndices.append(i)
            touchedIndices.append(i + 1)

    print(a, b, a + b)
    return a + b
# todo this is an incomplete solution
assert solution("RLLLLRRRLR") == 3 # 3
assert solution("RLRRLLRLRL") == 4 # 4
assert solution("LLLLRRRR") == 1 # 1
solution("RRLRRLRLLLRL")

