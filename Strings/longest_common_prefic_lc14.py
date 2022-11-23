# Longest Common Prefix
# Leetcode 14
# https://leetcode.com/problems/longest-common-prefix/

def longest_common_prefic_lc14(strs: list[str]) -> str:
    """Write a function to find the longest common prefix string amongst an array of strings.

    If there is no common prefix, return an empty string "".

    Time complexity: O(n^2) [check each letter of each word]
    Space complexity: O(n) [array of common letters]

    :param strs: The list of strings
    :type strs: list[str]

    :rtype: str
    :return: Longest common prefix of strs' strs
    """
    if not strs:
        return ""

    letters: list[str] = [] # list of letters that are known to be common so far

    first_word: str = strs[0]
    i: int = 0
    while i < len(first_word):
        this_letter = first_word[i]

        # check all other words
        for j in range(1, len(strs)):
            this_word: str = strs[j]
            if i >= len(this_word) or this_word[i] != this_letter:
                # reached end of word / found a non-common letter
                return ''.join(letters)

        letters.append(this_letter)
        i += 1

    return ''.join(letters)
