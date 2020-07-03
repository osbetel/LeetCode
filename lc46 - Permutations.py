def permute(nums: [int], orig_len):
    """
    :param nums: input list
    :param orig_len: the length of the original input list.
        Determines which permutations go in the final result
    :return: all possible ORDERINGS of the input list eg: [1,2,3] -> [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

    approach: we have the list nums as a source, L = len(nums). We are essentially
    doing nPr(L, L) on nums. --> nPr(n, r) = n! / (n - r)!
    To do this, we sample recursively.
    permute([1,2,3])      -> take [1] + permute([2,3])
      permute([2,3])      -> take [2] + permute([3])
          permute([3])    -> return [3] -> return [2,3] -> [1,2,3]
      permute([2,3])      -> take [3] + permute([2])
          permute([2])    -> return [2] -> return [3,2] -> [1,3,2]
    permute([1,2,3])      -> take [2] + permute([1,3])... etc
    ...
    """

    L = len(nums)
    if L == 1: return nums
    permutations = []
    for i in range(0, L):
        curr = [nums[i]]
        remaining = nums[:i] + nums[i + 1:]

        for x in permute(remaining, orig_len):
            if L != orig_len:
                curr.append(x)
                permutations.append(curr)
            else:
                permutations.append(curr + x)

    return permutations


# This is a newer, a lot more elegant solution using DFS. Technically the above solution
# is also a DFS but clearly it's kinda janky.
def permute2(nums):
    permutations = []
    dfs(nums, [], permutations)
    return permutations


def dfs(nums, path, res):
    # initially [1,2,3], [], []
    if not nums:
        # path is filled
        res.append(path)
    for i in range(len(nums)):
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
