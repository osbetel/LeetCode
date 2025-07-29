"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets. 

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""

from typing import List
def threeSumNaive1(nums: List[int], target: int = 0) -> List[List[int]]:
    # approach? naive approach is to generate all combinations of i, j, k and then check all of them
    # first how do we generate the set of all indices?
    def combinations(nums, k):
        if k == 0:
            return [[]]
        if not nums:
            return []
        
        first = nums[0]
        remainder = nums[1:]
        with_first = [[first] + combination for combination in combinations(remainder, k - 1)]
        without_first = combinations(remainder, k)
        return with_first + without_first
    
    res = []
    # gets all possible indice combinations, then we sum and add to result. hard to check for uniqueness of sums, see example 1
    all_possible_indices = combinations(range(len(nums)), 3)
    for api in all_possible_indices:
        vals = sorted([nums[i] for i in api])
        if sum(vals) == target and vals not in res:
            res += [vals]
    return res


def threeSumNaive2(nums: List[int], target: int = 0) -> List[List[int]]:
    # this is also a brute force approach that looks like three pointers approach
    #   - Outer loop: i runs n times, averaging O(n)
    #   - Middle loop: j runs from i to n, averaging n/2 times
    #   - Inner loop: k runs from j to n, averaging n/3 times
    # O(n) x O(n/2) x O(n/3) = O(n^3)
    assert len(nums) >= 3
    res = []
    total = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            for k in range(j, len(nums)):
                if i < j < k:
                    total += 1
                    s = nums[i] + nums[j] + nums[k]
                    # print(nums[i], nums[j], nums[k], s)
                    if s == target:
                        res.append(sorted([nums[i], nums[j], nums[k]]))

    uniques = list(set(tuple(r) for r in res))
    return [list(x) for x in uniques]
        

def threeSumDFS(nums: List[int], target: int = 0) -> List[List[int]]:
    # Graph traversal approach: treat each array index as a node
    # DFS to find all paths of length 3 that sum to target
    result = []
    
    def dfs(path, used_indices, current_sum, remaining_depth):
        # Base case: found a triplet
        if remaining_depth == 0:
            if current_sum == target:
                result.append(sorted(path[:]))  # Add sorted triplet
            return
        
        # Explore all unused indices (graph edges)
        for i in range(len(nums)):
            if i not in used_indices:
                path.append(nums[i])
                used_indices.add(i)
                dfs(path, used_indices, current_sum + nums[i], remaining_depth - 1)
                # Backtrack
                path.pop()
                used_indices.remove(i)
    
    # Start DFS from each possible starting index
    for start_idx in range(len(nums)):
        dfs([nums[start_idx]], {start_idx}, nums[start_idx], 2)
    
    # Remove duplicates by converting to set of tuples
    unique_triplets = list(set(tuple(triplet) for triplet in result))
    return [list(triplet) for triplet in unique_triplets]


def threeSumBFS(nums: List[int], target: int = 0) -> List[List[int]]:
    # BFS approach: use queue to explore paths level by level
    from collections import deque
    result = []
    
    # Queue stores: (path, used_indices, current_sum, depth)
    queue = deque()
    
    # Initialize queue with each starting index
    for start_idx in range(len(nums)):
        queue.append(([nums[start_idx]], {start_idx}, nums[start_idx], 1))
    
    while queue:
        path, used_indices, current_sum, depth = queue.popleft()
        
        # If we've reached depth 3, check if sum equals target
        if depth == 3:
            if current_sum == target:
                result.append(sorted(path[:]))
            continue
        
        # Explore all unused indices for next level
        for i in range(len(nums)):
            if i not in used_indices:
                new_path = path + [nums[i]]
                new_used = used_indices | {i}
                new_sum = current_sum + nums[i]
                queue.append((new_path, new_used, new_sum, depth + 1))
    
    # Remove duplicates
    unique_triplets = list(set(tuple(triplet) for triplet in result))
    return [list(triplet) for triplet in unique_triplets]
        

def threeSumPointers(nums: List[int], target: int = 0) -> List[List[int]]:
    # Optimal O(n^2) solution using sort + two pointers
    nums.sort()  # O(n log n)
    res = set()

    for i in range(len(nums)): # i represents the first pointer, ie the first choice
        left, right = i + 1, len(nums) - 1  # represent second and third choices to meet the target
        
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s == target:
                res.add((nums[i], nums[left], nums[right]))
                
                # this is used to remove the duplicates in the output,
                # eg: [[-1, -1, 2], [-1, 0, 1], [-1, 0, 1]] => [[-1, 0, 1], [-1, -1, 2]]
                # while left < right and nums[left] == nums[left + 1]:
                #     left += 1
                # while left < right and nums[right] == nums[right - 1]:
                #     right -= 1
                    
                left += 1
                right -= 1
            elif s < target:
                # smaller than target, need to add more, move left pointer up
                left += 1
            else:
                # greater than target, need to remove some, move right pointer down
                right -= 1
            # print(i, left, right, s)

    # uniques = list(set(tuple(r) for r in res))
    # return [list(x) for x in uniques]
    return [list(x) for x in res]


tests = [
    [-1,0,1,2,-1,-4],
    # [0,1,1],
    # [0, 0, 0],
]
for t in tests:
    print(threeSumPointers(t))