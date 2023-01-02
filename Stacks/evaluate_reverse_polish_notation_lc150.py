# Evaluate Reverse Polish Notation
# Leetcode 150
# https://leetcode.com/problems/evaluate-reverse-polish-notation/

def evaluate_reverse_polish_notation_lc150(tokens: list[str]) -> int:
    """ You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

    Evaluate the expression. Return an integer that represents the value of the expression.

    Note that:

    The valid operators are '+', '-', '*', and '/'.
    Each operand may be an integer or another expression.
    The division between two integers always truncates toward zero.
    There will not be any division by zero.
    The input represents a valid arithmetic expression in a reverse polish notation.
    The answer and all the intermediate calculations can be represented in a 32-bit integer.

    Time Complexity: O(n)
    Space Complexity: O(n)

    :param tokens: List of operators and operands
    :type tokens: list[str]

    :rtype: int
    :return: The evaluated solution to the reverse polish notation equation
    """
    stack: list[int] = []

    ops = {
        '+': lambda a, b : a + b,
        '-': lambda a, b : a - b,
        '*': lambda a, b : a * b,
        '/': lambda a, b: int(a / b)
    }

    for token in tokens:
        if token in ops:
            # Operator
            b = stack.pop()
            a = stack.pop()

            stack.append(ops[token](a, b))
        else:
            # Operand
            stack.append(int(token))

    return stack.pop()            