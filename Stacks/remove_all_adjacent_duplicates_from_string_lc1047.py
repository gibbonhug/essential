# Make The String Great
# Leetcode 1047
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

def remove_all_adjacent_duplicates_from_string_lc1047(s: str) -> str:
    """You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

    We repeatedly make duplicate removals on s until we no longer can.

    Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

    (Essentially same problem as Make The String Great)

    Time complexity: O(n)
    Space complexity: O(n)

    :param s: The string to remove adjacent duplicates from
    :type s: str

    :rtype: str
    :return: String after removing adjacent duplicates
    """
    stack: list[str] = []

    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)

    return "".join(stack)