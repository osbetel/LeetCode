





def twoSum(nums, target):
    # give a 1-indexes array of ints, sorted in non decreasing order
    # find two numbers such that they add up to a specific target
    # return the indices (1 indexed!) as an array [a, b]
    # there is always a guaranteed solution, element can't be used twice
    d = {}
    for i in range(len(nums)):
        x = nums[i]
        y = target - x
        if y in d:
            return [d[y] + 1, i + 1]
        else:
            d.update({x: i})


nums = [-1,0]
target = -1
print(twoSum(nums, target))

