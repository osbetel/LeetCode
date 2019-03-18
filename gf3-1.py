import time

def answer(s, l):
    # s is the start number, from 0 to 2,000,000,000
    # length of nums to be processed is always equal to length of the checkout line squared
    # ie: the total number of people to be checked is l^2
    # where s is the starting number, and subsequent numbers are sequential from s
    # example: if s = 5 and l = 2, then the numbers are 5, 6, 7, 8, and we return 5^6^7.
    # Another example, if l = 4 then we XOR the following slots:
    # x x x x
    # x x x -
    # x x - -
    # x - - -
    # Since the total number of IDs is l^2, and IDs only run from 0 to 2 billion,
    # then the closest round number to sqrt(2 billion) = 44,721. This is the maximum value for l,
    # likewise, the maximum ID value is 2,000,000,000, which means that the longest possible loop
    # is with a starting ID of 0 and a length of 44,721 for a total of 1,999,967,841 loops
    return checksum5(s, l)


def checksum5(s, l):
    # You know google, I was really hoping to avoid going into a mathematical solution with the bits
    # of the relevant integers...
    #
    # Since the numbers are sequential and a row is always of length l, we can find a pattern to XOR only the numbers that
    # will matter. ie: only some numbers in a row will actually change the checksum. Lets see if I can't cut
    # time complexity to less than N^2 / 2
    #
    # Supposing s = 0, l = 5, then these are the numbers we XOR together for the checksum.
    #
    # s        0  1  2  3  4   (s + l - 1)      XOR = 4b = 0100 = 0^4
    # s + l    5  6  7  8  -   (s + 2l - 2)     XOR = 12b = 1100 = 5^8^1
    # s + 2l   10 11 12 -  -   (s + 3l - 3)     XOR = 13b = 1101 = 12^1
    # s + 3l   15 16 -  -  -   (s + 4l - 4)     XOR = 31b = 11111 = 15^16
    # s + 4l   20 -  -  -  -   (s + 5l - 5)
    # ...                    ...
    # Thus we can see a general formula for the first number in the row is s + (n-1)l,
    # And a formula for the last number in the row is (s + nl - n), where n is the number of the row (starting at 1)
    #
    # So per loop, we can say s increments by l (s += l) which gives the first number in the row.
    # For the last number, it would be the value s + l - c - 1, since s increments by l each loop.
    #
    # There is also a pattern to the values of the XOR results per row. It's more evident with larger values of l,
    # If s is even, then the resulting XOR of that row can be ^last, ^1, ^last^1, ^0.
    # Conversely with odd values of s, which only occur if the initial input s or l is odd,
    # We can have values of ^first, ^first^last, ^(first - 1)^last, ^first^1

    checksum = 0
    for c in xrange(0, l):
        lastInRow = s + l - c - 1
        # print(s, lastEle)
        # print(str(s) + " : " + str(bin(s)), str(lastInRow) + " : " + str(bin(lastInRow)))

        if s == lastInRow: return checksum^s

        if s % 2 == 0:
            a = [lastInRow, 1, lastInRow^1, 0]
        else:
            a = [s, s^lastInRow, s^1, (s - 1)^lastInRow]
        checksum ^= a[(lastInRow - s) % 4]

        s += l
    return checksum

def checksum4(s, l):
    # You know google, I was really hoping to avoid going into a mathematical solution with the bits
    # of the relevant integers...
    #
    # Since the numbers are sequential and a row is always of length l, we can find a pattern to XOR only the numbers that
    # will matter. ie: only some numbers in a row will actually change the checksum. Lets see if I can't cut
    # time complexity to less than N^2 / 2


    checksum = 0
    for c in reversed(xrange(1, l + 1)):
        lastEle = s + c - 1  # by starting xrange reversed, we can eliminate the l in (s + l - c - 1)
        # print(str(s)+ " : " + str(bin(s)), str(lastEle)+ " : " + str(bin(lastEle)))
        # print(s,lastEle)
        if s == lastEle:
            checksum ^= s
        else:
            if s % 2 == 0:
                a = [lastEle, 1, lastEle ^ 1, 0]
            else:
                a = [s, s ^ lastEle, s - 1, (s - 1) ^ lastEle]
            # print(a, (j - s) % 4)
            checksum ^= a[(lastEle - s) % 4]
        s += l
    return checksum
    # checksum(0, 44000) == 2145452032


def checksum3(s, l):
    # given length of l, we can imagine a big l x l square. So there are l x l people total
    # starting id is s. For the first row we process l people, second row we process l - 1,
    # third row we process l - 2... And so on, taking all their IDs and XOR'ing them to the checksum.
    # So we need a counter that starts at l and decrements per loop.
    # We also need to move s up by l per loop.
    # And when the counter = 0 then we stop.
    # for example if l = 4:
    #       s           x       x       x
    #       s + l       x       x       -
    #       s + 2l      x       -       -
    #       s + 3l      -       -       -
    #
    # Execution times
    # 1.1e-05   (l = 10)
    # 0.000227  (l = 100)
    # 0.021832  (l = 1000)
    # 2.093241  (l = 10000)
    # tests 3, 4, 5 still exceed the time limit. Make it better or else.
    # for 3, 4, 5, l is > 50,000 based on my tests. 50 seconds to crunch 50,000 is too long.
    # a for loop executing 50,000 times takes 0.171468 seconds.
    # time complexity of the function below is still N^2 / 2, which is better than N^2 but for larger N's
    # it doesn't matter.

    checksum = 0
    counter = l
    while counter > 0:
        for idx in xrange(s, s + counter):
            if idx > 2000000000:
                return checksum
            checksum ^= idx
        s += l
        counter -= 1
    return checksum

def checksum2(s, l):
    # Execution time... Even slower. I am garbage.
    # 1.33333333333e-05 (l = 10)
    # 0.00121866666667  (l = 100)
    # 0.114437666667    (l = 1000)
    # 11.7746546667     (l = 10000)
    #
    # Also of N^2 time complexity.

    checksum = 0
    i = 0
    j = 0
    counter = 0
    for idx in xrange(0, l ** 2):
        # every l loops, reset i back to 0.
        # every l loops, increment j
        # print(counter, i, j s + idx)
        if counter == l:
            i = 0
            j += 1
            counter = 0

        if (i + j) < l:
            checksum ^= (s + idx)
            i += 1
        counter += 1
    return checksum


def checksum1(s, l):
    # This solution is too slow for four tests! Tests 3, 4, 5, 10 must contain large values of l
    # which causes a too-long execution time. Find something more efficient...
    # time complexity is currently N^2 which is far too high to use nested for loops for large amounts like that
    #
    # execution time in seconds
    # 2.8e-05   (l = 10)
    # 0.000951  (l = 100)
    # 0.086991  (l = 1000)
    # 8.804267  (l = 10000)

    checksum = 0
    i = 0
    for idx1 in range(0, l):
        for idx2 in range(0, l):
            if (idx1 + idx2) < l:
                checksum ^= (s + i)
            i += 1
    return checksum


def timer(x):
    start = time.clock()
    print("function return: " + str(answer(0, x)))
    end = time.clock()
    print("execution time (s): " + str(end - start))

# timer(17)
# timer(1000)
# timer(10000)
# timer(44000)
timer(8)


# xrange()
# 1.5e-05
# 0.000817
# 0.084782
# 8.389457
