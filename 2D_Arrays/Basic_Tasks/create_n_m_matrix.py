# Basic Task: Create an empty (0-filled) n * m matrix

def create_n_m_matrix(n: int, m: int) -> list[list[int]]:
    """Return an n*m sized matrix, empty (full of 0's)

    :param n: The number of rows of matrix
    :type n: int
    :param m: The number of cols of matrix
    :type m: int

    :rtype: list[list[int]]
    :return: An empty/0-valued n*m matrix
    """
    # List comprehension: create n (row#) m-lengthed (col#) matrices, with 0 as values
    empty_matrix: list[int[int]] = [[0 for col in range(len(matrix[0]))] for row in range(len(matrix))]

    return empty_matrix