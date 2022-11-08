# Three Sum
# Leetcode 15
# https://leetcode.com/problems/3sum/

def three_sum_lc15(nums: list[int]) -> list[list[int]]:
    """Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

    Notice that the solution set must not contain duplicate triplets.

    Time complexity: O(nlogn) [sorting]
    Space complexity: O(n) [disregard sorting]

    :param nums: The list of nums to search
    :type nums: list[int]

    :rtype: list[list[int]]
    :return: list containing unique triplets in nums which sum to 0
    """
    nums.sort() # 3 Sum 2.5: Two Sum 1.5.2
    res: list[list[int]] = []

    last_first_num = None

    for i in range(len(nums)-1): # must be at least 2 nums left
        first_num: int = nums[i]

        # no duplicates
        if first_num == last_first_num:
            continue

        # Two Sum 2
        target: int = 0 - first_num

        left: int = i + 1
        rite: int = len(nums) - 1
        
        while (left < rite):
            if nums[left] + nums[rite] < target:
                left += 1
            elif nums[left] + nums[rite] > target:
                rite -= 1
            else:
                res.append([first_num, nums[left], nums[rite]])

                # no duplicates
                last_used_second_num = nums[left]
                while nums[left] == last_used_second_num and left < rite:
                    left += 1 

        last_first_num = first_num

    return res