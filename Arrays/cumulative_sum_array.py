def cumulative_sum_array(nums: list[int]) -> list[int]:
    """Given a list of nums, return a list which represents the cumulative sum in nums at that index

    Example: [0, 1, 4, 0, 3] -> [0, 1, 5, 5, 8]

    Time complexity: O(n)
    Space complexity: O(n)

    :param nums: The list of nums
    :type nums: list[int]

    :rtype: list[int]
    :return: Cumulative sum list
    """
    if not nums:
        return []
    
    cuum_sum_list: list[int] = [nums[0]]

    for i in range(1, len(nums)):
        cuum_sum_here = nums[i] + cuum_sum_list[i-1]
        cuum_sum_list.insert(i, cuum_sum_here)

    return cuum_sum_list