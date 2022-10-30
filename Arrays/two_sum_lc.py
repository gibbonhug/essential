# Two Sum
# Leetcode 1
# https://leetcode.com/problems/two-sum/

def two_sum_lc(nums: List[int], target: int) -> List[int]:
    """Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.

    :param nums: The list of nums to search
    :type nums: List[int]
    :param nums: The target value
    :type nums: int

    :rtype: List[int]
    :return: List containing the 2 indices in nums with values that sum to target
    """
    seen_num_map: {int: int} = {}

    for i in range(0, len(nums)):
        num: int = nums[i]
        diff: int = # the number we need to make this num add up to target

        if diff in seen_num_map:
            return [seen_num_map[diff], i]
        else:
            seen_num_map[num] = i