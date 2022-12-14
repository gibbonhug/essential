# Basic Task: Determine whether an array contains a 'mirror' value / duplicate etc

# Two Sum
# Leetcode 1
# https://leetcode.com/problems/two-sum/

def two_sum_lc1(nums: list[int], target: int) -> list[int]:
    """Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.

    Time complexity: O(n)
    Space complexity: O(n)

    :param nums: The list of nums to search
    :type nums: list[int]
    :param nums: The target value
    :type nums: int

    :rtype: list[int]
    :return: list containing the 2 indices in nums with values that sum to target
    """
    seen_num_map: {int: int} = {}

    for i, num in enumerate(nums):
        diff: int = target - num # the number we need to make this num add up to target

        if diff in seen_num_map:
            return [seen_num_map[diff], i]
        else:
            seen_num_map[num] = i