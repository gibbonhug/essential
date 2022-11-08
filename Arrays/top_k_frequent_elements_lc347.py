# Top K Frequent Elements
# Leetcode 347
# https://leetcode.com/problems/top-k-frequent-elements/

def top_k_frequent_elements(nums: list[int], k: int) -> list[int]:
    """Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

    Time complexity: O(n)
    Space complexity: O(n) [new hashmap & array of len n]

    :param nums: The list of nums
    :type nums: list[int]
    :param nums: The top k frequent elements to return [ie k = 2: return 1st most frequent and 2nd most frequent]
    :type nums: int

    :rtype: list[int]
    :return: list of top k most frequent elements in nums
    """
    # first count how many times each num occurs; map each num to its count
    occ_map: {int: int} = {}
    for num in nums:
        occ_map[num] = 1 + occ_map.get(num, 0)
    
    # then bucket sort with occs; index: occ; element: list of number/s with that count
    # ie, index 0: nums that appear 0 times; 1: nums that appear 1 time, etc
    occ_to_num: list[list[int]] = [[] for i in range(len(nums) + 1)]

    for num, occ in occ_map.items():
        occ_to_num[occ].append(num)

    res: list[int] = []

    # go from highest -> lowest occurances until we find k nums
    for i in range(len(occ_to_num) - 1, 0, -1):
        for num in occ_to_num[i]:
            res.append(num)
        
        if len(res) == k:
                return res
