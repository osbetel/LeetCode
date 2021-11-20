
class Solution:
    @staticmethod
    def removeDuplicates1(nums: [int]) -> int:
        offset = 0
        for idx in range(len(nums) - 1):
            current = nums[idx - offset]
            next = nums[idx - offset + 1]
            if current == next:  # they're the same, remove one
                nums = nums[:idx - offset] + nums[idx - offset + 1:]
                offset += 1
                # constraint is that we don't use any further memory
                # even though we are taking list slices this actually does not use any further memory
                # slices are not copies of a list, and we can prove this by examining references with the following
                # l = ["a", "b", "c"]
                # print(list(map(id, l))
                # l = [:-1]
                # print(list(map(id, l))
                # references are the same, no copies are made in memory, rather we just trim the list
                # internally this I believe just changes some bytes to cut the memory allocation of the
                # array from 3 elements to 2 elements, thus not using any additional memory
        return nums


# nums = [1,2,2,3,3,3,4,4,5,6,7,8,8,8]
# nums = [1,2,2,2,3,4]
# k = Solution.removeDuplicates(nums)
# print(nums)
# print(k)



