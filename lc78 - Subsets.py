def recursive_top_down_gen_powerset(elements, powerset):
    # how can we recursively generate the powerset from a list of elements?
    # we will construct new subsets and add them to the powerset
    # suppose we have a list of 3 elements, [1,2,3]
    # first we start with the empty set [], then we add all sets of size 1, [1], [2], [3],
    # then sets of size 2, [1, 2], [1, 3], [2, 3],
    # then sets of size 3, [1,2,3]
    # we can see then that this problem has an optimal substructure. That is, starting from sets of size 3,
    # [1,2,3], we can actually construct all sets of size 2, and all sets of size 1, and the empty set,
    # by eliminating elements.
    # this is actually known as the backtracking method (almost, need to eliminate redundant recursive branches)

    if elements not in powerset:
        powerset.append(elements)

    for i in range(len(elements)):
        subset = elements[:i] + elements[i+1:]
        if subset in powerset:
            continue
        else:
            powerset.append(subset)
        recursive_top_down_gen_powerset(subset, powerset)
    return powerset


def bottom_up_constructive_gen_powerset(elements):
    # this method constructs the subsets one element at a time
    # start with [[]], then consider the first element 1
    # we produce [[], [1]], then consider the element 2,
    # which produces [] + 2 = [2], and [1] + 2 = [1,2]
    # resulting in [[],[1], [2], [1,2]]... and so on
    ps = [[]]
    for e in elements:
        ps.extend([subset + [e] for subset in ps])
    return ps


a = [1,2,3,4,5,6,7]

import time
start = time.process_time()

# ps = bottom_up_constructive_gen_powerset(a)
rps = recursive_top_down_gen_powerset(a, [])

end = time.process_time()
print(end - start)