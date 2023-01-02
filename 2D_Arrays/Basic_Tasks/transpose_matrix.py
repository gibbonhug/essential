# Basic Task: Transpose a matrix (exchange rows for cols, vice versa)

def transpose_matrix(matrix: list[list[int]]) -> list[list[int]]:
    """Given a matrix, return the transpose of that matrix

    :param matrix: The original matrix to transpose
    :type matrix: list[list[int]]

    :rtype: list[list[int]]
    :return: The transposed matrix (rows exchanged for cols)
    """
    # Version 1: zip
    # *matrix equivalent to matrix[0], matrix[1], ... , matrix[len(matrix) - 1]
    # zip function does the work of transposing matrix
    transpose: list[list[int]] = zip(*matrix)

    # Version 2: List comprehension

    transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

    return transpose