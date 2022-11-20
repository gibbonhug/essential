# Ugly Number
# Leetcode 263
# https://leetcode.com/problems/ugly-number/

def ugly_number_lc263() -> bool:
    """An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

    Given an integer n, return true if n is an ugly number.

    Time Complexity: O(logn)
    Space Complexity: O(1)

    :param n: The number
    :type n: int

    :rtype: bool
    :return: Whether n is ugly
    """
    if n <= 0:
        return False

    while n % 2 == 0:
        n /= 2

    while n % 3 == 0:
        n /= 3

    while n % 5 == 0:
        n /= 5

    return n == 1