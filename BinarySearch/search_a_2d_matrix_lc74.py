# Search a 2D Matrix
# Leetcode 74
# https://leetcode.com/problems/search-a-2d-matrix/

# Unfinished (no comments)

def search_a_2d_matrix_lc74(matrix: list[list[int]], target: int) -> bool:
    """You are given an m x n integer matrix matrix with the following two properties:

    Each row is sorted in non-decreasing order.
    The first integer of each row is greater than the last integer of the previous row.

    iven an integer target, return true if target is in matrix or false otherwise.

    You must write a solution in O(log(m * n)) time complexity.

    Time Complexity: O(log(m*n)) 
    Space Complexity: O(1)

    :param matrix: The matrix to search
    :type matrix: list[list[int]]
    :param target: The target integer
    :type target: int

    :rtype: bool
    :return: Whether matrix contains the target number
    """
    NUM_ROW = len(matrix)
    NUM_COL = len(matrix[0])

    lo_bo = 0
    hi_bo  = NUM_ROW - 1
    found_row = None

    while lo_bo <= hi_bo:
        # Search middle row each iteration within ro bounds
        row = lo_bo + ((hi_bo - lo_bo) // 2)

        # Check greatest value in current row
        if target > matrix[row][-1]:
            lo_bo = row + 1
        # Check smallest value in current row
        elif target < matrix[row][0]:
            hi_bo = row - 1
        # Else target is within current row
        else:
            found_row = row
            break

    # Never broke, target not in any row, return False
    if found_row is None:
        return False

    # Binary Search on the found_row

    lo = 0
    hi = NUM_COL - 1

    while lo <= hi:
        mid = lo + ((hi - lo) // 2)

        this_num = matrix[found_row][mid]

        if target > this_num:
            lo = mid + 1
        elif target < this_num:
            hi = mid - 1
        else:
            return True

    return False