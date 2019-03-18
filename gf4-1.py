import time

# Write a function of the form answer(times, time_limit) to calculate the most bunnies you can pick up and which
# bunnies they are, while still escaping through the bulkhead before
# the doors close for good. If there are multiple sets of bunnies of the same size, return the set of bunnies
# with the lowest prisoner IDs (as indexes) in sorted order. The bunnies
# are represented as a sorted list by prisoner ID, with the first bunny being 0. There are at most 5 bunnies, and
# time_limit is a non-negative integer that is at most 999.
#
# For instance, in the case of
# [
#   [0, 2, 2, 2, -1],  # 0 = Start
#   [9, 0, 2, 2, -1],  # 1 = Bunny 0
#   [9, 3, 0, 2, -1],  # 2 = Bunny 1
#   [9, 3, 2, 0, -1],  # 3 = Bunny 2
#   [9, 3, 2, 2,  0],  # 4 = Bulkhead
# ]
# and a time limit of 1, the five inner array rows designate the starting point, bunny 0, bunny 1, bunny 2, and
# the bulkhead door exit respectively. You could take the path:
# Start End Delta Time Status
#     -   0     -    1 Bulkhead initially open
#     0   4    -1    2
#     4   2     2    0
#     2   4    -1    1
#     4   3     2   -1 Bulkhead closes
#     3   4    -1    0 Bulkhead reopens; you and the bunnies exit


def answer(times, timeLimit):
    # times = 2D matrix, each element of the matrix is an array representing a bunny.
    # index is the bunny's prisoner ID number.
    # ie: times[0] = bunny 0, times[1] = bunny 1.
    # each bunny array consists of a series of integer representing the time taken to travel to that location
    # eg: suppose times[0][0] = [0, 2, 2, 2, -1] corresponding to [start, bunny 0, bunny 1, bunny 2, bulkhead]
    # There can be at most 5 bunnies. So the max size is [start, b0, b1, b2, b3, b4, bulkhead]
    # bulkhead value is time delta. So -1 is +1 to the timer, and 1 is -1 to the timer

    # Thus, with the start, the bulkhead, and up to 5 bunnies, the resulting matrix is always a square matrix
    # L x L, where L = # bunnies + 2 (for the start and bulkhead values)
    # it also has a dividing diagonal from top left to bottom right, of only 0's,
    # indicating that travel time from a node to itself is always 0.

    # Lets break down the function:
    # The first way that comes to mind is to model this using a graph with edges and vertices,
    # Followed by something similar to djikstra's algorithm to find the optimal path.
    # I'd just need to add a caveat that it must touch as many vertices as possible and reach the end with a time of 0 or more

    # It could also potentially be modeled as a DFA/NFA where the 0 times would represent epsilon paths.
    # Those epsilon paths are useless though (no need to go from bunny 2 to bunny 2), but the DFA/NFA model could be feasible

    # However, we don't need to return the path that the character takes to acquire the bunnies, just return as an array
    # which bunnies you can get. Which means that the bunnies you can get is a subset of all the bunnies given,
    # S <= B, where B is all bunnies given.

    # First order of business: acquire all the subsets of possible nodes you can hit
    # ie, for bunnies of 0, 1, 2, we can have S = {(), (0), (1), (2), (0, 1), (0, 2), (1, 2), (0, 1, 2)}, where |S| = 8.
    # This means that if b = the number of bunnies, the size of set S = 2^b.
    # The formula [nCr(b,1) + nCr(b, 2) + ... + nCr(b,b) + 1] is behind it, so you can see how the power-set is generated

    pset = powerSet(times) # the return value must be in here somewhere. How do we determine?

    # given an element of pset, eg: if pset = P({0, 1, 2}), then suppose we select (0, 1, 2), then the number of ways
    # we can reach all nodes is nPr(3, 3) = 6 or (0,1,2), (0,2,1), (1,0,2), (1,2,0), (2,0,1), (2,1,0)

    possible = []
    solutions = []
    for p in pset:
        if p != ():
            # for b in xrange(0, len(p) + 1):
            #     p.append("b")
            # p = [0, 1, 'b', 'b', 'b']
            paths = nPrSets(p)
            # paths = removeExtraBees(paths)

            import itertools
            paths = list(paths for paths,_ in itertools.groupby(paths))
            paths.sort()
            print(paths)
            for route in paths:
                possible.append(testPath(times, timeLimit, route))
            break

    possible.sort()
    for ps in possible:
        if ps != -1: solutions.append(removeAllBees(ps))
    solutions.sort(key=len, reverse=True)
    if len(solutions) > 0:
        return solutions[0]
    else: return []


def removeAllBees(ls):
    # start = time.clock()
    tmp = []
    for x in ls:
        if x != "b": tmp.append(x)

    # end = time.clock()
    # print("removeAllBees(): " + str(end - start))
    return tmp


def removeExtraBees(paths):
    # start = time.clock()
    tmp = []
    lenPaths = 0
    lenP = 0
    for p in paths:
        lenPaths += 1
        # p = [0,1,2,"b","b","b","b"]
            # if not (p[idx] == "b" and p[idx + 1] == "b"):
        # print(p)
        if not any(p[idx] == "b" and p[idx + 1] == "b" for idx in range(len(p)-1)):
            lenP += 1
            tmp.append(p)
            # break
    # end = time.clock()
    # print("removeExtraBees(): " + str(end - start))
    # print(lenPaths)
    # print(lenP)
    return tmp


def testPath(times, cost, path):
    # path given as a tuple containing numbers representing bunny IDs.
    # bunny IDs are simply the index of the times matrix - 1
    # start = time.clock()
    startIdx = 0
    for idx in path:
        if idx != "b":
            i = idx + 1
            cost -= times[startIdx][i]
            # print(startIdx, i, cost)
            startIdx += (i - startIdx)
        else:
            i = len(times) - 1
            cost -= times[startIdx][i]
            # print(startIdx, i, cost)
            startIdx += (i - startIdx)

    # end = time.clock()
    # print("testPath(): " + str(end - start))
    if cost >= 0:
        # print(path)
        return path
    else:
        return -1


def addBees(listOfBunnies):
    # start = time.clock()
    finalResult = []
    result = []

    for n in xrange(2*len(listOfBunnies) - 1):
        result = listOfBunnies[:]
        for b in xrange(0, len(result) - 1):
            result.insert(2*b - 1, "b")

    result.append("b")
    finalResult.append(result)
    # end = time.clock()
    # print("addBees(): " + str(end - start))
    return finalResult


def nPrSets(s):
    # start = time.clock()
    import itertools as i
    perm = i.permutations(s, len(s))
    # return list(list(tup) for tup in perm)
    # end = time.clock()
    # print("nPrSets(): " + str(end - start))
    return perm


def powerSet(s):
    # start = time.clock()
    elements = []
    for idx in xrange(0, len(s)):
        if idx != 0 and idx != len(s) - 1:
            elements.append(idx - 1)
    import itertools as i

    l = list((list(tup) for tup in list(reversed(list(
        i.chain.from_iterable(i.combinations(elements, b) for b in xrange(len(elements) + 1))
    )))))

    # end = time.clock()
    # print("powerset(): " + str(end - start))
    return l


def timer(fx, *args):
    import time
    total = 0
    tests = 100
    for n in xrange(tests):

        start = time.clock()
        fxr = fx(*args)
        print("function return: " + str(fxr))
        end = time.clock()
        print("execution time (s): " + str(end - start))
        total += (end - start)

    print("Average time(s): " + str(total/tests))
    return fxr

times = [
    [0,2,2,2,-1],
    [9,0,2,2,-1],
    [9,3,0,2,-1],
    [9,3,2,0,-1],
    [9,3,2,2,0]
    ]

times2 = [
    [0,2,2,1,2,-1],
    [9,0,2,2,2,-1],
    [9,3,0,7,3,-1],
    [9,3,3,0,1,-1],
    [9,3,1,4,0,-1],
    [9,3,2,1,2,0],
    ]

times3 = [[0, -5, 200, 200, 200],
         [200, 0, 1, 200, 200],
         [200, 200, 0, 1, 200],
         [1, 200, 200, 0, 200],
         [200, 200, 200, 200, 0]]

times4 = [
    [0,2,2,1,2,2,-1],
    [9,0,2,2,2,2,-1],
    [9,3,0,7,3,2,-1],
    [9,3,3,0,1,2,-1],
    [9,3,1,4,0,2,-1],
    [9,3,2,1,2,1,0],
    ]

times5 = [
    [0,2,2,1,2,2,-1],
    [9,0,2,2,2,2,-1],
    [9,3,0,7,3,2,-1],
    [9,3,3,0,1,2,-1],
    [9,3,1,4,0,2,-1],
    [9,3,2,1,2,1,0],
    ]
timer(answer,times5, 10000)
# print(answer(times,1))



