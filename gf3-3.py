


def answer3(l):

    if 3 > len(l) > 2000: return 0
    triples = 0
    executions = -2

    for idy in xrange(1, len(l) - 1):

        idx = 0
        idz = idy + 1
        x = 0
        z = 0

        while idx < idy:
            if l[idy] % l[idx] == 0:
                x += 1
            idx += 1
            executions += 1

        while idz < len(l):
            if l[idz] % l[idy] == 0:
                z += 1
            idz += 1
            executions += 1

        triples += (x * z)
    # print(executions)

    return triples

# number of executions where n is length of list l is: (n * (n - 3) + 2) or (n^2 - 3n +2)
def answer2(l):
    if 2000 < len(l) < 3: return 0

    triples = 0
    executions = 0
    for i in xrange(1, len(l) - 1):
        x = 0
        z = 0

        for j in xrange(0, i):
            # print(j,i)
            executions += 1
            if l[i] % l[j] == 0:
                x += 1

        for k in xrange(i + 1, len(l)):
            executions += 1
            if l[k] % l[i] == 0:
                z += 1
        triples += (x * z)
    # print(executions)
    return triples

b = [1,2,3,4,5,6]
# print(answer2(b))
# print(answer3(b))

def combinations(listLength, sampleSize):
    import math
    return math.factorial(listLength) / (math.factorial(sampleSize) * math.factorial(listLength - sampleSize))

def timer(fx, *args):
    import time
    start = time.clock()
    fxr = fx(*args)
    print("function return: " + str(fxr))
    end = time.clock()
    print("execution time (s): " + str(end - start))
    return fxr

def test():
    import random
    fxr = 0
    while fxr == 0:
        b = []
        length = 100
        while len(b) < length:
            b.append(random.randint(1, 999999))
        fxr = timer(b)

def testOnce():
    import random
    b = []
    length = 1000
    while len(b) < length:
        b.append(random.randint(1,999))
    timer(answer3, b)
    # print(b)
# test()
testOnce()

# print(combinations(100,3))
