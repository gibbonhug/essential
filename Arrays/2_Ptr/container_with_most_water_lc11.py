# Container With Most Water
# Leetcode 11
# https://leetcode.com/problems/container-with-most-water/

def container_with_most_water_lc11(height: list[int]) -> int:
    """You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

    Find two lines that together with the x-axis form a container, such that the container contains the most water.

    Return the maximum amount of water a container can store.

    Notice that you may not slant the container.

    Time Complexity: O(n)
    Space Complexity: O(1)

    :param height: The list of heights of the lines
    :type nums: list[int]

    :rtype: int
    :return: The greatest amount of 'rain water' which can be trapped
    """
    left: int = 0
    rite: int = len(height) - 1

    max_water_seen: int = 0

    while left < rite:
        shorter_line: left if height[left] < height[rite] else rite
        width = rite - left
        
        this_area = height[shorter_line] * width

        max_water_seen = max(this_area, max_water_seen)

        # always keep tallest line; change shorter line
        if shorter_line == left:
            left += 1
        else:
            rite -= 1

    return max_water_seen