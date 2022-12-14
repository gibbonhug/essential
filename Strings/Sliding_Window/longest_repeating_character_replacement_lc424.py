# Longest Repeating Character Replacement
# Leetcode 424
# https://leetcode.com/problems/longest-repeating-character-replacement/

def longest_repeating_character_replacement_lc424(s: str, k: int) -> int:
    """You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

    Return the length of the longest substring containing the same letter you can get after performing the above operations.

    Unoptimized solution (see youtube video)

    Time complexity: O(26 * n)
    Space complexity: O(26) [dictionary with 26 keys maximum]

    :param prices: The string to perform operation on
    :type prices: str
    :param k: Number of characters which can be replaced in a given substring of s
    :type k: int

    :rtype: int
    :return: Longest substring of s containing same char given at most k replacements
    """
    char_occ: {str: int} = {}

    l: int = 0

    max_len: int = 0

    for r in range(len(s)):
        char_occ[s[r]] = char_occ.get(s[r], 0) + 1
        len_max_occ: int = max(char_occ.values())

        # r - l + 1: length of current substring

        if (r - l + 1) - len_max_occ > k:
            # shrink window
            char_occ[s[l]] -= 1
            l += 1

        max_len = max(max_len, (r - l + 1))

    return max_len

def longest_repeating_character_replacement_lc424_bruteforce(s: str, k: int) -> int:
    """You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

    Return the length of the longest substring containing the same letter you can get after performing the above operations.

    Brute Force Solution

    Time complexity: O(n^2)
    Space complexity: O(26) [dictionary with 26 keys maximum]

    :param prices: The string to perform operation on
    :type prices: str
    :param k: Number of characters which can be replaced in a given substring of s
    :type k: int

    :rtype: int
    :return: Longest substring of s containing same char given at most k replacements
    """
    max_len: int = 0

    # i: start index of this substring
    for i in range(len(s)):
        # map chars to occs
        this_map: {str: int} = {}

        # j: length of this substring past first char
        # Loop thru all Consecutive Substrings: See Arrays/Basic_Tasks/consecutive_subarrays
        for j in range(0, len(s) - i):
            this_char: str = s[i+j]
            this_map[this_char] = this_map.get(this_char, 0) + 1
            
            # length of this substring + 1: include first char
            this_len: int = j + 1

            # analyzing this substring will not increase our max, so ignore 
            # and go to next
            if this_len <= max_len:
                continue

            # find occ of char which appears most often in this substring
            len_max_occ: int = max(this_map.values())

            num_chars_to_replace: int = this_len - len_max_occ

            if num_chars_to_replace <= k:
                max_len = this_len # already know this_len is > than existing max_len

    return max_len