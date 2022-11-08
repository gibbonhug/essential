# Make The String Great
# Leetcode 1544
# https://leetcode.com/problems/make-the-string-great/

def make_the_string_great_lc1544(s: str) -> str:
    """Given a string s of lower and upper case English letters.

    A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

        0 <= i <= s.length - 2
        s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.

    To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.

    Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

    Notice that an empty string is also good.

    Time complexity: O(n)
    Space complexity: O(n)

    :param s: The string to make good
    :type s: str

    :rtype: str
    :return: Good version of parameter string
    """
    stack = []

    for char in s:
        # test if lowercase/uppercase pair
        if stack and abs(ord(stack[-1]) - ord(char)) == 32:
            stack.pop()
        else:
            stack.append(char)
            
    return (''.join(stack))