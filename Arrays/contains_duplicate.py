# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# Leetcode 217
# https://leetcode.com/problems/contains-duplicate/

def containsDuplicate(nums: list[int]) -> bool:
    """
    :type nums: List[int]
    :rtype: bool
    """
    seen_nums = set()

    for num in nums:
        if num in seen_nums:
            return True
        else:
            seen_nums.add(num)

    # no value appears at least twice
    return False
