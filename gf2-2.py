
# given a list of positive integers l, and a target integer t
# find the first sublist whose integers sum up to t.
# Constraints:
# each list l will contain at least 1 and up to 100 ints
# target t is not more than 250
# all elements of l and t are positive
#
# (int list) l = [4, 3, 10, 2, 8]
# target t = 12
# returns [2, 3]
#
# (int list) l = [4, 3, 5, 7, 8]
# target t = 12
# returns [0, 2], even if there is a shorter list summing to 12 [2, 3],
# always returns the first occurrence

def answer(l, t):
    # l = [4, 3, 5, 7, 8]
    # t = 12

    if sum(l) < t:
        return [-1, -1]

    s = 0
    start = 0
    end = 0

    while True:
        # start at first index, check if the following numbers can add to target
        for k in l[start:]:
            print(start, end, s)
            if s < t and end <= len(l): # end = len(l) if t can't be found
                s += k
                end += 1 # moving the end index with each iteration, tallying a sum
            elif s == t:
                return [start, end - 1]
            elif s > t: # sum of slice [start:end] overflowed past target.
                s = 0   # Reset and increment starting index
                start += 1
                end = start
                break   # no need to finish looping the rest if we reset and increment
            elif end > len(l) and s != t:
                # start index has gotten to the end of the line and target not found?
                # print("end of the line")
                return [-1, -1]







l = [4, 3, 5, 7, 8]
t = 12
# print(answer(l, t))

l = [4, 5, 10, 5, 8]
t = 17
print(answer(l, t))



