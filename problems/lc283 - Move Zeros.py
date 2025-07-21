



def moveZeros(nums):
    # given an integer array of nums, move all zeros to the end
    # maintaining relative order of other elements
    idx = 0
    iterations = 0
    while idx < len(nums):
        if iterations > len(nums):
            break
        else:
            iterations += 1

        if nums[idx] == 0:
            nums.append(0)
            nums.pop(idx)
            continue
        idx += 1
        print(idx, nums)
    return nums


nums = [0,1,2,0,0,0,0,4,5,1,6,0,1]
print(moveZeros(nums))



