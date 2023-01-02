# Basic Task: Iterate through the rows of a 2D Array (Matrix)

def rows_of_matrix(matrix: list[list[int]]) -> list[list[int]]:
    """Return a list containing the rows of a 2D matrix as lists. (Equivalent to returning the original list.)

    :param matrix: The matrix to find rows from
    :type matrix: list[list[int]]

    :rtype: list[list[int]]
    :return: List containing the rows of the matrix as lists.
    """
    if not matrix:
        return []

    list_of_rows: list[list[int]] = []

    # 1 version: Loop
    for row in matrix:
        #  Problem-specific code here
        list_of_rows.append(row)

    list_of_rows = []

    # 2 version: Another loop
    for i in range(len(matrix)):
        this_row = matrix[i]
        # Problem-specific code here
        list_of_rows.append(this_row)

    # 3 version: List comprehension
    list_of_rows = [row for row in matrix]

    return list_of_rows