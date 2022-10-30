# Contains duplicate
# Leetcode 217
# https://leetcode.com/problems/contains-duplicate/

def contains_duplicate_lc(nums: List[int]) -> bool:
    """Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

    :param arr: The list of ints to search
    :type nums: List[int]

    :rtype: bool
    :return: Boolean corresponding to whether nums contains duplicate values
    """
    seen_nums = set()

    for num in nums:
        if num in seen_nums:
            return True
        else:
            seen_nums.add(num)

    # no value appears at least twice
    return False
