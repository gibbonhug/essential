# Group Anagrams
# Leetcode 49
# https://leetcode.com/problems/group-anagrams/

#unfinished
def group_anagrams_lc49(strs: list[str]) -> list[list[str]]:    
    """Given an array of strings strs, group the anagrams together. You can return the answer in any order.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.  

    Time complexity: O(
    Space complexity: O(

    :param strs: The list of strings to search for group anagrams
    :type strs: list[str]

    :rtype: list[list[str]
    :return: list containing sublists which group anagrams together, eg [['cat', 'tac'], ['rat', 'tar', 'art']]
    """
    charocc_to_strs: {list[str] : list[str]} =  {} # map alphabet (index) occurance : its associated strings in strs

    for word in strs:
        this_charocc: list[int] = [0] * 26
        # populate this_charocc
        for char in word:
            char_index: int = ord(char) - ord('a')
            this_charocc[char_index] += 1

        this_charocc_tuple: tuple = tuple(this_charocc) # lists cannot be keys

        if this_charocc_tuple in charocc_to_strs:
            charocc_to_strs[this_charocc_tuple].append(word)
        else:
            charocc_to_strs[this_charocc_tuple] = [word]

    return charocc_to_strs.values()