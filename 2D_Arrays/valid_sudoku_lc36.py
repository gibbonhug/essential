# Valid Sudoku
# Leetcode 36
# https://leetcode.com/problems/valid-sudoku/

def valid_sudoku_lc36(board: list[list[int]]) -> bool:
    """Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

    Time complexity: O(n^2) n == 9
    Space complexity: O(n^2) n == 9

    :param board: list of rows (also lists) of rows of sudoku board
    :type board: list[list[int]]

    :rtype: bool
    :return: whether board is valid sudoku per constraints of problem
    """
    row_to_seen_nums = collections.defaultdict(set) # keys = row_num ; vals = set of seen ints in this row
    col_to_seen_nums = collections.defaultdict(set) # keys = col_num ; vals = set of seen ints in this col
    sqr_to_seen_nums = collections.defaultdict(set)  # keys = (r_n // 3, c_n // 3) tuple  ; vals = set of seen ints in this square

    # 9 x 9 grid
    for row_num in range(9):
        for col_num in range(9):
            this_num = board[row_num][col_num]

            if this_num == ".":
                continue
            
            if (
                this_num in row_to_seen_nums[row_num] or 
                this_num in col_to_seen_nums[col_num] or 
                this_num in sqr_to_seen_nums[(row_num // 3, col_num // 3)]
            ):
                return False

            row_to_seen_nums[row_num].add(this_num)
            col_to_seen_nums[col_num].add(this_num)
            sqr_to_seen_nums[(row_num // 3, col_num // 3)].add(this_num)

    return True