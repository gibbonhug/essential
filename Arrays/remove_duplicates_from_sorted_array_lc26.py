# Remove Duplicates from Sorted Array
# Leetcode 26
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

def remove_duplicates_from_sorted_array_lc26(nums: list[int]) -> int:
    """Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

    Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

    Return k after placing the final result in the first k slots of nums.

    Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

    Time complexity: O(n^2)
    Space complexity: O(1)

    :param nums: The list of nums to 'remove duplicates' from
    :type nums: list[int]

    :rtype: int
    :return: Number of 'unique' elements in nums (length of nums - # of numbers that are not the first instance of a particular number)
    """
    unique_position: int = 1 # first element is 'unique'
    i: int = 0

    for i in range(len(nums) - 1):
        if nums[i+1] != nums[i]:
            nums[unique_position] = nums[i+1]
            unique_position += 1

    while i < len(nums) - 1:
        i += 1

    return unique_position