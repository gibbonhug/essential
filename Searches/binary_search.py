# Binary Search (iterative and recursive implementations)
# Time complexity: O(logn) [worst, avg]; O(1) [best: goal in mid of arr]
# Space complexity: O(1)

def binary_search_iterative(arr: list[int], goal: int) -> int:
    """Returns the index of goal within list. If goal does not exist within the list, returns -1.
    
    :param arr: The list of ints to search
    :type arr: list[int]
    :param goal: The int to search for
    :type goal: int

    :rtype: int
    :return: The index of goal within the list if it exists; if not, -1
    """
    lo: int = 0
    hi: int = len(arr) - 1

    while (lo <= hi):
        mid: int = lo + ((hi - lo) // 2) # avoid overflow

        if (arr[mid] == goal):
            return mid
        elif (arr[mid] < goal):
            lo = mid + 1
        elif (arr[mid] > goal):
            hi = mid - 1

    # goal is not in arr
    return -1

def binary_search_recursive(arr: list[int], goal: int, lo: int = 0, hi: int = None) -> int:
    """Returns the index of goal within list. If goal does not exist within the list, returns -1.
    This function should not be called with lo or hi parameters; calling with anything other than default values for lo and hi will likely return an incorrect result

    :param arr: The list of ints to search
    :type arr: list[int]
    :param goal: The int to search for
    :type goal: int
    :param lo: The lower index in the portion of list being searched
    :type lo: int
    :param hi: The higher index in the portion of list being searched
    :type hi: int

    :rtype: int
    :return: The index of goal within the list if it exists; if not, -1
    """
    # set default parameter
    if (hi is None):
        hi = len(arr) - 1

    # binary search
    if (lo <= hi):
        mid: int = lo + ((hi - lo) // 2)

        if arr[mid] == goal:
            return mid
        elif arr[mid] < goal:
            return (binary_search_recursive(arr, goal, mid + 1, hi))
        elif arr[mid] > goal:
            return (binary_search_recursive(arr, goal, lo, mid - 1))

    # goal is not in arr
    return -1