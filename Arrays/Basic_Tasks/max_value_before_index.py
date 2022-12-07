# Basic Task: Given a list of nums, construct an array of the maximum value seen before 
# the current index. Set the 0th index of the array as 0

def max_value_before_index(nums: list[int]) -> list[int]:
    """Given a list of nums, construct an array of the maximum value seen before 
        the current index. Set the 0th index of the array as 0

    Example: [0, 1, 4, 0, 3] -> [0, 0, 1, 4, 4]

    Time complexity: O(n)
    Space complexity: O(n)

    :param nums: The list of nums
    :type nums: list[int]

    :rtype: list[int]
    :return: Described list
    """
    res: list[int] = [0] * len(nums)

    for i in range(1, len(nums)):
        res[i] = max(nums[i-1], nums[i-1])

    return res