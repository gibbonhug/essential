# Longest Substring Without Repeating Characters
# Leetcode 3
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

def longest_substring_without_repeating_characters_lc3(s: str) -> int:
    """Given a string s, find the length of the longest substring without repeating characters.

    A substring is a contiguous non-empty sequence of characters within a string.

    Time complexity: O(
    Space complexity: O(

    :param s: String
    :type s: str

    :rtype: int
    :return: Length of longest substring of s without repeating characters
    """
    char_set: set(str) = set()

    longest_len: int = 0

    left: int = 0

    for rite in range(len(s)):
        while s[rite] in char_set:
            char_set.remove(s[left])
            left += 1
        
        char_set.add(s[rite])

        longest_len = max(longest_len, rite - left + 1)

        # the longest possible substring starting from the 
        # current char at left index is shorter than the longest
        # string we have seen, so wasting time to continue
        if (len(s) - left) < longest_len:
            break

    return longest_len