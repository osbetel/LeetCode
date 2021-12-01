






def containsDuplicate1(nums):
    # two approaches
    # 1) sort the list, iterate
    # 2) hash or set
    if len(set(nums)) == len(nums):
        return False
    return True

def containsDuplicate2(nums):
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return False
    return True

def containsDuplicate3(nums):
    d = set()
    for x in nums:
        if x in d:
            return True
        d.add(x)
    return False



