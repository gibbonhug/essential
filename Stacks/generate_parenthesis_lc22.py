# Generate Parenthesis
# Leetcode 22
# https://leetcode.com/problems/generate-parentheses/

# unfinished

def generate_parenthesis_lc22(n: int) -> list[str]:
    """Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

    Time Complexity: O(n^2) (?)
    Space Complexity: O(n^2) (?)

    :param n: How many pairs of parenthesis
    :type n: int

    :rtype: list[str]
    :return: List of all combos of well-formed parenthesis
    """
    stack: list[str] = []
    res: list[str] = []

    def backtrack(num_open: int, num_close: int) -> str:
        if (num_open == num_close == n):
            # valid set of parenthesis the len of n
            res.append("".join(stack))
            return
        
        if num_open < n:
            stack.append("(")
            backtrack(num_open+1, num_close)
            stack.pop() # go back up tree 

        if num_close < num_open:
            stack.append(")")
            backtrack(num_open, num_close+1)
            stack.pop() # go back up tree 

    backtrack(0, 0) # start with 0 parenthesis added

    return res