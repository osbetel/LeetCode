def permute2(nums):
    """
    Difference between lc47 and lc46 is that this one is required to handle duplicates.
    For example, if we are given [1,1,1], lc46 code would return 6 copies of that same list
    because it assumes all elements are unique.
    We should only be returning unique permutations.
    """
    permutations = []
    dfs(nums, [], permutations)
    return list(set(permutations))  # literally change this. set removes duplicates, list turns it back to a list


def dfs(nums, path, res):
    # initially [1,2,3], [], []
    if not nums:
        # path is filled
        res.append(tuple(path))     # and change this. Can't do set(permutations) unless
    for i in range(len(nums)):      # they're tuples. lists are not hashable, tuples are.
        # suppose nums = [1,2,3]
        # for each i paths splits into len(nums) branches recursively
        # paths -> [1], rem = [2, 3], etc.
        remainder = nums[:i] + nums[i + 1:]
        dfs(remainder, path + [nums[i]], res)


import time
l = [1,2,3]

now = time.time()
p = permute2(l)
print(p)
after = time.time()
print("exec time: ", after - now)
