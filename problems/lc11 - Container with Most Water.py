"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of 
the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1
"""
from typing import List
def maxArea(height: List[int]) -> int:
    # approach - two pointers, start one at the left and right sides
    # calculate area and save it
    # move pointer of the smaller value inwards. logic being that moving the larger pointer can't possibly improve
    # the result. if heights are equal just move the left one or something
    # O(n) time complexity, O(1) space in this case
    if not height:
        return 0

    # areas = []
    max_area = 0
    left, right = 0, len(height) - 1
    while left < right:
        width = right - left
        max_height = min(height[left], height[right])
        area = width * max_height
        max_area = max(max_area, area)
        # areas.append([width, height[left], height[right], area])

        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1
    return max_area


tests = [
    [1,8,6,2,5,4,8,3,7],
    # [1,1]
]

for t in tests:
    print(maxArea(t))