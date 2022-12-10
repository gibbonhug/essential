# Trapping Rain Water
# Leetcode 42
# https://leetcode.com/problems/trapping-rain-water/

def trapping_rain_water_lc42(height: list[int]) -> int:
    """Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

    Time Complexity: O(n)
    Space Complexity: O(1)

    :param height: The list of heights
    :type nums: list[int]

    :rtype: int
    :return: The total amount of 'rain water' which will be trapped
    """
    res: int = 0

    l: int = 0 # index of left
    r: int = len(height) - 1 # index of rite

    max_left: int = height[l]
    max_rite: int = height[r]

    while l < r:
        if max_left < max_rite:
            l += 1
            max_left = max(max_left, height[l])
            # calc height of bar for area (width of each bar is 1)
            res += max_left - height[l] 
        else:
            r -= 1
            max_rite = max(max_rite, height[r])
            # calc height of bar for area (width of each bar is 1)
            res += max_rite - height[r]
        
    return res

def trapping_rain_water_lc42_list(height: list[int]) -> int:
    """Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

    Time Complexity: O(n)
    Space Complexity: O(2n) = O(n)

    :param height: The list of heights
    :type nums: list[int]

    :rtype: int
    :return: The total amount of 'rain water' which will be trapped
    """
    max_left: List[int] = [0] * len(height)
    max_rite: List[int] = [0] * len(height)

    # See Arrays/Basic_Tasks/max_value_before_index
    for i in range(1, len(height)):
        max_left[i] = max(height[i-1], max_left[i-1])

    for i in range(len(height) - 2, -1, -1):
        max_rite[i] = max(height[i+1], max_rite[i+1])

    res: int = 0
        
    for i in range(len(height)):
        # water in this i block will be limited by height of the
        # shorter tallest parent on l,r side of this block
        water_here: int = min(max_left[i], max_rite[i]) - height[i]
    
        res += max(0, water_here)

    return res