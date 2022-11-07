import re

# Valid Palindrome
# Leetcode 242
# https://leetcode.com/problems/valid-palindrome/

def valid_palindrome_lc243(s: str) -> bool:
    """A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

    Given a string s, return true if it is a palindrome, or false otherwise.

    :param s: The string to determine whether palindrome
    :type s: str

    Time complexity: O(len(s))
    Space complexity: O(1)

    :rtype: bool
    :return: Boolean value corresponding to whether strings s is a palindrome, with regard to its alphanumeric chars
    """
    left: int = 0
    rite: int = len(s) - 1

    while left <= rite:
        while left <= rite and not s[left].isalnum():
            left += 1

        while left <= rite and not s[rite].isalnum():
            rite -= 1

        if s[left].lower() != s[rite].lower():
            return False

        left += 1
        rite -= 1

    return True

def valid_palindrome_recursive_lc243(s: str) -> bool:
    """A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

    Given a string s, return true if it is a palindrome, or false otherwise.

    Recursive implementation. Exceeds timelimit, due to stripping non-alphanumerics being slow.

    Time complexity: O(1) [disregard stripping non-alphanumerics]
    Space complexity: O(len(s)) [recursive calls] [disregard stripping non-alphanumerics]

    :param s: The string to determine whether palindrome
    :type s: str

    :rtype: bool
    :return: Boolean value corresponding to whether strings s is a palindrome, with regard to its alphanumeric chars
    """
    # testing if char is/not alnum is tedious recursively, outside scope of question;
    # this line strips non alnums from s
    s = ''.join(ch for ch in s if ch.isalnum()) 

    # "" is a palindrome ; "a", where a is any character, is a palindrome
    if len(s) == 0 or len(s) == 1:
        return True

    # if s has 2 chars, it is a palindrome if its chars are equal: 
    if len(s) == 2:
        return s[0].lower() == s[1].lower()

    left: int = 0
    rite: int = len(s) - 1

    return valid_palindrome_recursive_lc243(s[left] + s[rite]) and valid_palindrome_recursive_lc243(s[left+1:rite])