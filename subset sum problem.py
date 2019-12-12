
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



a = [1,2,2,3,5,1,6,2,3,4,5,76,8,523,2,3,5,3,5,2,3,6,6,23,45,4,5,23,5,35,7,45,34,5,34,56,34,5,345,34,5,34,5]
# a = [2,3,4,5,6,7,8,2,3,5,2,9,6,9,1,3,3,5,6,3]

import time
start = time.process_time()

# ps = gen_powerset(a)
# print(does_powerset_contain_target_sum(ps, 800))
print(isSubsetSum(a, len(a), 1))

end = time.process_time()
print(end - start)




