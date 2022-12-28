# Product Of Array Except Self
# Leetcode 238
# https://leetcode.com/problems/product-of-array-except-self/

def product_of_array_except_self_lc238(nums: list[int]) -> list[int]:
    """Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

    You must write an algorithm that runs in O(n) time and without using the division operation.

    Time complexity: O(n)
    Space complexity: O(n) | O(1) per leetcode disregarding res array

    :param nums: The list of nums
    :type nums: list[int]

    :rtype: list[int]
    :return: Array answer such that answer[i] is equal to the product of all the elements of nums except nums[i] 
    """
    if not nums:
        return []

    res: list[int] = [1 for i in range(len(nums))]

    # prefix: product of array before this i element
    prefix: int = 1
    for i in range(len(nums)):
        res[i] = prefix # start prefix at 1
        prefix *= nums[i] # for next loop

    # postfix: product of array after this i element
    # (multply old prefix at res[i] by prefix to get product except self)
    postfix: int = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]

    return res
    