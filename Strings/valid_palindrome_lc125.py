# Valid Palindrome
# Leetcode 242
# https://leetcode.com/problems/valid-palindrome/

def valid_palindrome_lc243(s: str) -> bool:
    """A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

    Given a string s, return true if it is a palindrome, or false otherwise.

    :param s: The string to determine whether palindrome
    :type s: str

    :rtype: bool
    :return: Boolean value corresponding to whether strings s is a palindrome, with regard to its alphanumeric chars
    """
    left = 0
    rite = len(s) - 1

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