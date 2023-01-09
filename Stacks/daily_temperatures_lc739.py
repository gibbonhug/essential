# Daily Temperatures
# Leetcode 739
# https://leetcode.com/problems/daily-temperatures/

def daily_temperatures_lc739(temperatures: list[int]) -> list[int]:
    """Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

    Time Complexity: O(n)
    Space Complexity: O(n)

    :param temperatures: The given list of temperatures
    :type temperatures: list[int]

    :rtype: list[int]
    :return: List such that ith index is number of days after ith day to get a warmer temperature
    """
    # result array initialized with 0s initially
    # ("If there is no future day for which this is possible, 
    # keep answer[i] == 0 instead")
    res = [0 for i in range(len(temperatures))]

    # start with empty stack
    # stack's valies will be indices from temperatures
    stack = []

    for i in range(len(temperatures)):
        this_temp = temperatures[i]
        
        # Find all temps in the stack that this_temp is greater than
        # ("Looking/filling backwards")
        # (All numbers in stack will not already have an
        # increasing temperature after them)
        while stack and this_temp > temperatures[stack[-1]]:
            top = stack.pop()

            res[top] = i - top
        
        stack.append(i)

    return res