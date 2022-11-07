def increases_twice(nums: list[int]) -> bool:
    """Given an integer array nums, determine whether the array increases at least twice; that is, contains 3 ascending elements from its lowest to highest index.

    Example: [0, 1, 2] increases at least twice and would return true. [0, 1, 1] increases only once and would return false.

    Time complexity: O(n) [check entire list worst case]
    Space complexity: O(1)

    :param nums: The list of nums
    :type nums: list[int]

    :rtype: bool
    :return: Boolean value of whether nums increases twice
    """
    smallest = float('inf')
    second_smallest = smallest

    for num in nums:
        if num <= smallest:
            smallest = num
        elif num <= second_smallest:
            second_smallest = num
        else:
            return True
    
    return False