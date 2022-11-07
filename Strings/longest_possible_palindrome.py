def longest_possible_palindrome(strs: List[str]) -> int:
    """Given a list of two-character-long strings, determine the size of the longest possible palindrome that can be formed from these strings. Each string can occur more than once, and can be used at most however many times it appears in strs.

    strs = ["aa", "aa", "bb", "lf", "lf", "fl"] -> 10, because longest possible palindrome would be "flaabbaalf" or similar, which is 10 characters long.
    strs = ["aa"] -> 2, because longest possible palindrome "aa" is 2 chars
    strs = ["ab"] -> 0, because no palindrome can be formed from this list.

    Time complexity: O(n) [iterate over an array]
    Space complexity: O(n) [worst case: add every item in strs to sets]

    :param strs: The list of strings
    :type strs: List[str]

    :rtype: int
    :return: Size of longest possible palindrome to be formed from strs
    """
    sames = set() # for 'aa' type strings
    diffs = set() # for 'ab' type strings

    running_total = 0

    for word in strs:
        # 'aa' type string
        if word[0] == word[1]:
            if word in sames:
                sames.remove(word)
                running_total += 4 # 'aa' + 'aa' = 4
            else:
                sames.add(word)
        # 'ab' type string
        else:
            if word[::-1] in diffs: # find 'ba' for 'ab'
                diffs.remove(word[::-1])
                running_total += 4 # 'ab' + 'ba' = 4
            else:
                diffs.add(word)
    
    # if there are leftover 'words' in sames set, 1 and only 1 of these can be added to the final palindrome to maintain symmetry [split palindrome down middle, put 1 of these strs in the middle.]
    if sames:
        running_total += 2

    return running_total