# Two Sum II
# Leetcode 167
# https://leetcode.com/problems/two-sum/

def two_sum__ii_lc167(nums: list[int], target: int) -> list[int]:
    """Given an array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

    Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

    The tests are generated such that there is exactly one solution. You may not use the same element twice.

    Your solution must use only constant extra space.   

    Time complexity: O(n)
    Space complexity: O(1)

    :param nums: The list of nums to search
    :type nums: list[int]
    :param nums: The target value
    :type nums: int

    :rtype: list[int]
    :return: list containing the 2 indices in nums with values that sum to target
    """
    left: int = 0
    rite: int = len(nums) - 1
    
    while (left < rite):
        if nums[left] < nums[rite]:
            left += 1
        elif nums[left] > nums[rite]:
            rite -= 1
        else:
            return [left, rite]