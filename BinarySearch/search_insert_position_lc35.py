# Search Insert Position
# Leetcode 35
# https://leetcode.com/problems/search-insert-position/

def search_insert_position_lc35(nums: list[int], target: int) -> int:
    """Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

    You must write an algorithm with O(log n) runtime complexity.

    Time Complexity: O(logn)
    Space Complexit: O(1)

    :param nums: The list of nums
    :type nums: list[int]
    :param target: Target num
    :type target: int

    :rtype: int
    :return: Position of target (real or hypothetical)
    """
    left: int = 0
    rite: int = len(nums) - 1

    while left <= rite:
        mid: int = left + ((rite - left) // 2)

        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            rite = mid - 1
        else:
            return mid
        
    return left