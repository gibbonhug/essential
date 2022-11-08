# Product Of Array Except Self
# Leetcode 238
# https://leetcode.com/problems/product-of-array-except-self/

def product_of_array_except_self_lc238(nums: list[int]) -> list[int]:
    """Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

    You must write an algorithm that runs in O(n) time and without using the division operation.

    Time complexity: O(n
    Space complexity: O(

    :param nums: The list of nums
    :type nums: list[int]

    :rtype: list[int]
    :return: Array answer such that answer[i] is equal to the product of all the elements of nums except nums[i] 
    """
    if not nums:
        return []

    res: list = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]

    return res
    