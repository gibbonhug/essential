# Valid Parenthesis
# Leetcode 20
# https://leetcode.com/problems/valid_parenthesis/

def valid_parenthesis_lc20(s: str) -> bool:
    """Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

    Time complexity: O(n)
    Space complexity: O(n)

    :param s: The string to determine if valid parenthesis
    :type s: str

    :rtype: bool
    :return: Whether s is valid parenthesis
    """
    if (len(s) % 2 != 0):
        return False

    close_map = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    open_stack = []

    for char in s:
        if char not in close_map:
            open_stack.append(char)
            continue
        
        if not open_stack or open_stack.pop() != close_map.get(char):
            return False

    return not open_stack