# Permutation In String
# Leetcode 567
# https://leetcode.com/problems/permutation-in-string/

from Collections import counter

# Messy logic in code wrote while sleepy
def permutation_in_string_lc567(s1: str, s2: str) -> bool:
    """Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

    In other words, return true if one of s1's permutations is the substring of s2.

    Time complexity: O(len(s2))
    Space complexity: O(len(s1) + len(s2))

    :param s1: The string to check if a permutation is within s2
    :type s1:  str
    :param s2: The string to look for permutation of s1 within
    :type s2: str

    :rtype: bool
    :return: Whether s2 contains a contiguous permutation from the chars of s1
    """
    if (len(s2) < len(s1)):
           return False

    # map chars in s1 to their occurances
    s1_counter = Counter(s1)

    # build initial 

    left: int = 0
    rite: int = 0

    s2_cur_counter = {}

    for i in range(len(s1)):
        rite = i
        s2_char = s2[rite]

        s2_cur_counter[s2_char] = s2_cur_counter.get(s2_char, 0) + 1

    # actual logic of check if permutation
    if s2_cur_counter == s1_counter:
        return True

    while rite <= len(s2):
        # do not store 0 values in dictionary
        if s2_cur_counter[s2[left]] == 1:
            del s2_cur_counter[s2[left]]
        else:
            s2_cur_counter[s2[left]] -= 1

        left += 1

        rite += 1

        s2_cur_counter[s2[rite]] = s2_cur_counter.get(s2[rite], 0) + 1

        if s2_cur_counter == s1_counter:
            return True

    return False