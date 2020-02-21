
def powerset(seq, idx, curr_set, ps):
    if idx == len(seq):
        return ps


    ps.append(curr_set) # [1]

    for i in range(idx + 1, len(seq)):
        curr_set.append(seq[i]) # [2]
        powerset(seq, i, curr_set, ps)

    return ps


def isSubsetSum(set, n, sum):
    # Base Cases
    if (sum == 0):
        return True
    if (n == 0 and sum != 0):
        return False

    # If last element is greater than
    # sum, then ignore it
    if (set[n - 1] > sum):
        return isSubsetSum(set, n - 1, sum)

    # else, check if sum can be obtained
    # by any of the following
    # (a) including the last element
    # (b) excluding the last element
    return isSubsetSum(set, n - 1, sum) or isSubsetSum(set, n - 1, sum - set[n - 1])


# first, how can we generate the powerset of a list of elements?

def gen_powerset(elements):
    ps = [[]]
    for e in elements:
        ps.extend([subset + [e] for subset in ps])
    return ps


def recursive_gen_powerset(elements, powerset):
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
        if subset not in powerset:
            powerset.append(subset)
        recursive_gen_powerset(subset, powerset)
    return powerset


def does_powerset_contain_target_sum(ps, target):

    if target <= 0:
        return False

    current_total = 0
    num_sets_that_meet_criteria = 0
    for s in ps:
        for x in s:
            current_total += x
        if current_total == target:
            num_sets_that_meet_criteria += 1
            print(s, num_sets_that_meet_criteria)
            return True
        current_total = 0
    return False



# a = [1,2,2,3,5,1,6,2,3,4,5,76,8,523,2,3,5,3,5,2,3,6,6,23,45,4,5,23,5,35,7,45,34,5,34,56,34,5,345,34,5,34,5]
a = [2,3,4,5,6,7,8,9,10,11]
import time
start = time.process_time()

# ps = gen_powerset(a)
# print(len(ps))
rps = recursive_gen_powerset(a, [])
print(len(rps))

# print(does_powerset_contain_target_sum(ps, 1))
# print(isSubsetSum(a, len(a), 1))

end = time.process_time()
print(end - start)




