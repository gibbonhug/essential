# Longest Consecutive Sequence
# Leetcode 128
# https://leetcode.com/problems/longest-consecutive-sequence/

def longest_consecutive_sequence_lc128(nums: list[int]) -> int:
    """Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

    You must write an algorithm that runs in O(n) time.

    Time complexity: O(n) [iterating through array]
    Space complexity: O(n) [set from array]

    :param nums: The list of nums
    :type nums: list[int]

    :rtype: int
    :return: Length of longest consecutive subsequence to be found from nums in nums
    """
    nums_set: set(int) = set(nums)

    longest_seq_len: int = 0

    for num in nums:
        if num - 1 not in nums_set:
            this_seq_len: int = 1

            while num + this_seq_len in nums_set:
                this_seq_len += 1
        
            longest_seq_len = max(this_seq_len, longest_seq_len)

    return longest_seq_len
