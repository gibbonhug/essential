# Valid Anagram
# Leetcode 242
# https://leetcode.com/problems/valid-anagram/

def valid_anagram_lc242_hashmap(s: str, t: str) -> bool:
    """Given two strings s and t, return true if t is an anagram of s, and false otherwise.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

    Hashmap Implementation

    Time complexity: O(n) [iterate over an array]
    Space complexity: O(len(s)) [make two hash maps when len(s) == len(t)]

    :param s: The first string
    :type s: str
    :param t: The second string
    :type t: str

    :rtype: bool
    :return: Boolean value corresponding to whether strings s and t are anagrams
    """
    # can only be anagrams if same length
    if (len(s) != len(t)):
        return False

    # map char : occurance
    s_map: {str: int} = {} 
    t_map: {str: int} = {}

    for i in range(len(s)):
        s_char: str = s[i]
        t_char: str = t[i]

        # x_map.get(x_map[x_char], 0) will ret 0 iff x_char not in the map
        s_map[s_char] = 1 + s_map.get(s_map[s_char], 0)
        t_map[t_char] = 1 + t_map.get(t_map[t_char], 0)

    return (s_map == t_map)

def valid_anagram_lc242_sort(s: str, t: str) -> bool:
    """Given two strings s and t, return true if t is an anagram of s, and false otherwise.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

    Sort String Implementation

    Time complexity: O(nlogn) [sort string]
    Space complexity: O(1)
    
    :param s: The first string
    :type s: str
    :param t: The second string
    :type t: str

    :rtype: bool
    :return: Boolean value corresponding to whether strings s and t are anagrams
    """
    # can only be anagrams if same length
    if (len(s) != len(t)):
        return False

    s = sorted(s)
    t = sorted(t)

    for i in range(len(s)):
        if s[i] != t[i]:
            return False

    return True