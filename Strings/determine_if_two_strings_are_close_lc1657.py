from collections import Counter

# Determine if Two Strings Are Close
# Leetcode 1657
# https://leetcode.com/problems/determine-if-two-strings-are-close/

def determine_if_two_strings_are_close_lc1657(word1: str, word2: str) -> bool:
    """
    Two strings are considered close if you can attain one from the other using the following operations:

        Operation 1: Swap any two existing characters.
            For example, abcde -> aecdb
        Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
            For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)

    You can use the operations on either string as many times as necessary.

    Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

    Time complexity: O(n+m) [creating Counters]
    Space complexity: O(n+m), n: len(word1), m: len(word2)

    :param word1: The first word
    :type word1: str
    :param word2: The second word
    :type word2: str

    :rtype: bool
    :return: Whether the strings are 'close'

    """
    if len(word1) != len(word2):
        return False

    # Map each char to its occurances (testing Operation 1)
    w1_c_count = Counter(word1)
    w2_c_count = Counter(word2)

    # Map each occurance to its occurances (testing Operation 2)
    w1_o_count = Counter(w1_c_count.values())
    w2_o_count = Counter(w2_c_count.values())

    # Partially test operation 1
    if w1_c_count.keys() != w2_c_count.keys():
        return False

    # Testing o_counts == each other will also now test Operation 1 after if statement
    # I think
    return w1_o_count == w2_o_count