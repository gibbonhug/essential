# Basic Task: Iterate through the rows of a 2D Array (Matrix)

def rows_of_matrix(matrix: list[list[int]]) -> list[list[int]]:
    """Return a list containing the rows of a 2D matrix as lists. (Equivalent to returning the original list.)

    :param matrix: The matrix to find rows from
    :type matrix: list[list[int]]

    :rtype: list[list[int]]
    :return: List containing the rows of the matrix as lists.
    """
    list_of_rows: list[list[int]] = []

    # 1 version
    for row in matrix:
        list_of_rows.append(row)
    
    # reset
    list_of_rows = []

    # 2 version
    num_rows: int = len(matrix)

    for i in range(num_rows):
        this_row = matrix[i]
        list_of_rows.append(this_row)

    return list_of_rows