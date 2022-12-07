# Basic Task: Given a list of nums, construct an array of the maximum value seen before 
# the current index. Set the 0th index of the array as 0

def max_value_before_index(nums: list[int]) -> list[int]:
    """Given a list of nums, construct an array of the maximum value seen before 
        the current index. Set the 0th index of the array as 0

    Example: [0, 1, 4, 0, 3] -> [0, 0, 1, 4, 4]

    (Function could easily be modified to traverse array backwards and produce maximum value seen
    after current index)

    Time complexity: O(n)
    Space complexity: O(n)

    :param nums: The list of nums
    :type nums: list[int]

    :rtype: list[int]
    :return: List of nums representing maxmimum value seen in nums before that index (index 0 of this list is 0)
    """
    res: list[int] = [0] * len(nums)

    for i in range(1, len(nums)):
        res[i] = max(nums[i-1], res[i-1])

    return res