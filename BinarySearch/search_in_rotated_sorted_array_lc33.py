# Search In Rotated Sorted Array
# Leetcode 33
# https://leetcode.com/problems/search-in-rotated-sorted-array/

def search_in_rotated_sorted_array_lc33(nums: list[int], target: int) -> int:
    """There is an integer array nums sorted in ascending order (with distinct values).

    Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

    Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

    You must write an algorithm with O(log n) runtime complexity.

    Time Complexity: O(logn)
    Space Complexity: O(1)

    :param nums: The rotated sorted list of nums to search
    :type nums: list[int]
    :param target: The target number to find in nums
    :type target: int

    :rtype: int
    :return: The index of target in nums, if target is in nums, else -1
    """
    # indices
    l: int = 0
    r: int = len(nums) - 1
    
    # Binary Search (Searches/binary_search)
    while l <= r:
        mid: int = l  + ((r - l) // 2)
        
        if nums[mid] == target:
            return mid
        
        # search rest of array

        # mid is within left sorted portion
        elif nums[mid] >= nums[l]:
            # target is within left sorted portion (target is not mid):
            # move r to the -1 of mid
            if nums[l] <= target <= nums[mid]:
                r = mid - 1
            # target is not to the left of mid: 
            # move l to +1 of mid
            else:
                l = mid + 1
                
        # mid is within right sorted portion
        else:
            # target is within right sorted portion to right of mid:
            # move l to +1 of mid
            if nums[mid] <= target <= nums[r]:
                l = mid + 1
            # target is not to the right of mid:
            # move r to -1 of mid
            else:
                r = mid - 1
                
    # target is not in arr
    return -1 