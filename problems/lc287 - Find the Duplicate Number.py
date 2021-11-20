

# Given an array, nums, which contains n + 1 integers, where each integer is between 1 and n,
# there must be a duplicate integer. eg: if n = 4, then nums is 5 integers long,
# since each integer can only range from 1 - 4, we have nums = [1, 2, 3, 4, _], where the
# last space has to be filled with a duplicate integer
def findDuplicate(nums: [int]):

    s = set()
    for n in nums:
        if n in s:
            return n
        else: s.add(n)


# findDuplicate([1,3,4,2,2])