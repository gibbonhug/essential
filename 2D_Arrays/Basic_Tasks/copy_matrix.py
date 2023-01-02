# Basic Task: Copy a matrix by value

def copy_matrix(orig_matrix: list[list[int]]) -> list[list[int]]:
    """Given a parameter matrix, return a copy of this matrix

    :param orig_matrix: The original matrix to copy
    :type orig_matrix: list[list[int]]

    :rtype: list[list[int]]
    :return: A copy of the parameter matrix
    """
    copy = [row[:] for row in orig_matrix]

    return copy