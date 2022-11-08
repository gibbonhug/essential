# Basic Task: Iterate through the cols of a 2D Array (Matrix)

def cols_of_matrix(matrix: list[list[int]]) -> list[list[int]]:
    """Return a list containing the columns of a 2D matrix as lists. Order the columns from right to left ()

    :param matrix: The matrix to find cols from
    :type matrix: list[list[int]]

    :rtype: list[list[int]]
    :return: List containing the cols of the matrix as lists.
    """
    if not matrix:
        return []

    num_rows: int = len(matrix)
    num_cols: int = len(matrix[0])

    list_of_cols: list[list[int]] = []

    # j refers to the index of the current col
    for j in range(0, num_cols):
        this_col = []
        # i is the index of the row we are extracting int from relevant column
        for i in range(0, num_rows):
            this_col.append(matrix[i][j])
        
        list_of_cols.append(this_col)

    return list_of_cols