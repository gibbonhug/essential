# Linear Search (iterative and recursive implementations)

def linear_search(arr: list[int], goal: int) -> int:
    """Returns the index of goal within list. If goal does not exist within the list, returns -1.

    Time complexity: O(n) [worst, avg]; O(1) [best: goal in front of arr]
    Space complexity: O(1)

    :param arr: The list of ints to search
    :type arr: list[int]
    :param goal: The int to search for
    :type goal: int

    :rtype: int
    :return: The index of goal within the list if it exists; if not, -1
    """
    for i in len(arr):
        if arr[i] == goal:
            return i

    # goal is not in arr
    return -1

def linear_search_recursive(arr: list[int], goal: int, index: int = 0) -> int:
    """Returns the index of goal within list. If goal does not exist within the list, returns -1.
    Recursive implementation is for completeness' sake, as linear search is normally an iterative algorithm
    This function should not be called with index parameter; calling with anything other than the default value for index will likely return an incorrect result

    Time complexity: O(n) [worst, avg]; O(1) [best: goal in front of arr]
    Space complexity: O(n) [recursive calls] ; O(1) [best: goal in front of arr]

    :param arr: The list of ints to search
    :type arr: list[int]
    :param goal: The int to search for
    :type goal: int
    :param index: The current index we are checking, starting at 0
    :type index: int

    :rtype: int
    :return: The index of goal within the list if it exists; if not, -1
    """
    if (index < len(arr)):
        if (list[index] == goal):
            return index
        else:
            return(linear_search_recursive(arr, goal, index + 1))
            
    # goal is not in arr
    return -1