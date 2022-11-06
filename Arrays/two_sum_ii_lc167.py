# Two Sum II
# Leetcode 67
# https://leetcode.com/problems/two-sum/

def two_sum_lc67(nums: List[int], target: int) -> List[int]:
    """Given an array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

    Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

    The tests are generated such that there is exactly one solution. You may not use the same element twice.

    Your solution must use only constant extra space.   

    :param nums: The list of nums to search
    :type nums: List[int]
    :param nums: The target value
    :type nums: int

    :rtype: List[int]
    :return: List containing the 2 indices in nums with values that sum to target
    """
    left = 0
    rite = len(nums) - 1
    
    while (left < rite):
        if nums[left] < nums[rite]:
            left += 1
        elif nums[left] > nums[rite]:
            rite -= 1
        else:
            return [left, rite]