






def passwordStrength(pw):
    count = 0
    vowels = set(["a","e","i","o","u"])
    stack = []
    for i in range(len(pw)):
        if stack:
            # stack not empty, check current character and top of stack
            # if valid pair, +1, clear stack, else keep going
            if stack[-1] not in vowels and pw[i] in vowels:
                count += 1
                stack = []
            elif stack[-1] in vowels and pw[i] not in vowels:
                count += 1
                stack = []
        else:
            stack.append(pw[i])
    return count



# print(passwordStrength("hackerrank"))
# print(passwordStrength("thisisbeautiful"))
# print(passwordStrength("rhythm"))
# print(passwordStrength("bbabbabbabbabbabbab"))
# print(passwordStrength(""))


def applicationPairs(capacity, fg, bg):
    # naive implementation
    closest_sum = 0
    res = []
    for x in fg:
        for y in bg:
            z = x[1] + y[1]
            if capacity >= z >= closest_sum:
                closest_sum = z
                a = (x[0], y[0], z)
                res.append(a)
    if res:
        return [(x[0], x[1]) for x in res if x[2] == closest_sum]
    else:
        return [()]


mem = 10
fg = [[1,3],[2,5],[3,7],[4,10]]
bg = [[1,2],[2,3],[3,4],[4,5]]

print(applicationPairs(mem, fg, bg))


