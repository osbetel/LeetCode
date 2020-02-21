
def solution(A):
    # write your code in Python 3.6
    # so we essentially want to find slices of an array where every value in the prior slice is less than every value in the next
    # eg: if we have three slices A, B, C, then every value in slice A is less than every value in slice B, which is less than those in slice C,
    # and so on. This way we can sort the slices individually and be assured that their concatenation is sorted too.

    if not A:
        return 0

    # ok, new approach, we know the integers are distinct, but they don't necessarily start at a particular value. Could start from
    # 20 and skip a random number every time... So we can sort of identify
    min_arr = [0] * len(A)
    max_arr = [0] * len(A)
    l = len(A)
    min_arr[l - 1] = A[l - 1] # last element of minimums
    max_arr[0] = A[0]         # first element of maximums
    num_of_slices = 1
    # so the approach here is to iterate through the array A from the first element to the last (for maximum values)
    # and from the last element to the first for minimum values. Once we have these two arrays, we can scan through them for the
    # differences between "peaks" and "valleys" (I'm thinking of this like (x,y) coordinates...?). Every time we encounter one we
    # can increment the count of slices because it indicates an area where our slices A < B.
    for i in reversed(range(0, l - 1)):
        if A[i] <= min_arr[i + 1]:
            min_arr[i] = A[i]
        else:
            min_arr[i] = min_arr[i + 1]

    for i in range(1, l):
        if A[i] >= max_arr[i - 1]:
            max_arr[i] = A[i]
        else:
            max_arr[i] = max_arr[i - 1]

    # num_of_slices = 1
    for i in range(1, l):
        if min_arr[i] >= max_arr[i - 1]:
            num_of_slices += 1
    return num_of_slices


# a = [-1,-2,-3,-4] # 1
# b = [4,3,2,6,1] # 1
# c = [2, 4, 1, 6, 5, 9, 7] # 3
#
# print(solution(c))


def sol(S):

    if not s:
        return 10080

    arr = S.split("\n")
    numberline = []
    day_val = {"Mon": 0, "Tue": 1, "Wed": 2, "Thu": 3, "Fri": 4, "Sat": 5, "Sun": 6}

    # so I am essentially converting a single day and timeslot to an interval, and then finding the biggest gap between intervals
    for timestamp in arr:
        timestamp_split = timestamp.split(" ")
        day = day_val.get(timestamp_split[0]) * 24 * 60 # day offset converted into minutes
        hhmm = hhmm_hhmm_to_minutes(timestamp_split[1], day)
        numberline.append(hhmm)
    numberline.sort()

    # print(numberline) # uncomment to see. It saves times as intervals. The first example test is below
    #[[300, 780], [900, 1260], [1650, 2535], [2580, 2640], [3145, 3794],
    #[3794, 4240], [4320, 5759], [6060, 6360], [6750, 7190], [7320, 7560],
    #[7800, 8640], [8700, 8880], [9240, 9840]]
    biggest_gap = 0
    for i in range(len(numberline) - 1):
        left = numberline[i][1]
        right = numberline[i + 1][0]
        biggest_gap = max(biggest_gap, right - left)

    biggest_gap = max(biggest_gap, 10080 - numberline[len(numberline) - 1][1])

    return biggest_gap


def hhmm_hhmm_to_minutes(hhmm_hhmm, day):
    hhmm_hhmm = hhmm_hhmm.split("-")
    return [hhmm_to_minutes(hhmm_hhmm[0]) + day,  hhmm_to_minutes(hhmm_hhmm[1]) + day]


def hhmm_to_minutes(hhmm):
    hhmm = hhmm.split(":")
    return int(hhmm[0]) * 60 + int(hhmm[1])


s = """Sun 10:00-20:00
Fri 05:00-10:00
Fri 16:30-23:50
Sat 10:00-24:00
Sun 01:00-04:00
Sat 02:00-06:00
Tue 03:30-18:15
Tue 19:00-20:00
Wed 04:25-15:14
Wed 15:14-22:40
Thu 00:00-23:59
Mon 05:00-13:00
Mon 15:00-21:00"""

s2 = """Mon 01:00-23:00
Tue 01:00-23:00
Wed 01:00-23:00
Thu 01:00-23:00
Fri 01:00-23:00
Sat 01:00-23:00
Sun 01:00-21:00"""

s = ""
print(sol(s))



















