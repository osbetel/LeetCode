

def answer(s):
    # input string will be like s = ">------<"
    # output = 2. So imagine every tick, the arrows move in the direction they're facing by one space
    # if two arrows cross, they'll salute. Each arrow salutes once, so one pair of crossing arrows
    # salutes twice. Thus we can determine a solution by determining the number of crosses, and multiply by 2.

    sarr = list(s.strip("-")) # s.strip("-") removes extraneous "-" characters from the edges of the string
    count = 0
    result = 0
    # count counts how many arrows are going to the right ">".
    # Upon encountering an arrow going left "<", the count * 2 is added to the result.
    # All people walking left must pass all people walking to the right (that are ahead of them), and vice versa
    for sol in sarr:
        if sol == ">":
            count += 1
        elif sol == "<":
            result += (count * 2)
    return (result)



print(answer("---->-----<-")) # 2
print(answer("<<>><")) # 4
print(answer("--->-><-><-->-")) # 10

# s = "--->-><-><-->-"
# l = 0
# r = 0
# while s != "":
#     print(s, l, r)
#     s = s.strip("-")
#     if s[0] == "<" and s[len(s) - 1] == ">":
#         s = s[1:len(s) - 1]
#     elif s[0] == ">" and s[len(s) - 1] == ">":
#         s = s[0:len(s) - 2]
#     elif s[0] == "<" and s[len(s) - 1] == "<":
#         s = s[1:len(s) - 1]
# print(s, l ,r)
