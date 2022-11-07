def consecutive_zero_sum(nums: list[int]) -> int:
    """Given an integer array nums, determine the length of the longest sequence of consecutive ints that sum to zero. If no sequences sum to 0 in nums, return -1

    Examples: 
    [-1, 0, 1, 0, 1] -> 4: the sequence from i=0 to i=3 sums to 0 and is the longest sequence which sums to 0.
    [0, 0, 0] -> 3: The sequence from i=0 to i=2 is the longest sequence which sums to 0.
    [1] -> -1: No sequence in this array sums to 0

    Time complexity: O(
    Space complexity: O(

    :param nums: The list of nums
    :type nums: List[int]

    :rtype: int
    :return: Size of the longest consecutive sequence in nums which sums to 0
    """
    # empty list can't sum to 0
    if not nums:
        return -1

    # equivalent to cumulative_sum_array
    cuum_sum_list: list[int] = [nums[0]]
    for i in range(1, len(nums)):
        cuum_sum_here = nums[i] + cuum_sum_list[i-1]
        cuum_sum_list.insert(i, cuum_sum_here)

    return cuum_sum_list
