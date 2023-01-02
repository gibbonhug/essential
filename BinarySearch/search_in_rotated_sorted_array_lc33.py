# Search In Rotated Sorted Array
# Leetcode 33
# https://leetcode.com/problems/search-in-rotated-sorted-array/

def search_in_rotated_sorted_array_lc33(nums: list[int], target: int) -> int:
    """There is an integer array nums sorted in ascending order (with distinct values).

    Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

    Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

    You must write an algorithm with O(log n) runtime complexity.

    Time Complexity:
    Space Complexity:

    :param nums: The rotated sorted list of nums to search
    :type nums: list[int]
    :param target: The target number to find in nums
    :type target: int

    :rtype: int
    :return: The index of target in nums, if target is in nums, else -1
    """