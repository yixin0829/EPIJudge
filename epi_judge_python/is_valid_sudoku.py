from typing import List

from test_framework import generic_test


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    # TODO - you fill in here.
    # validate if a partially-complete sudoku is a valid sudoku
    def check_dups_row():
        for i in range(9):
            row = [ele for ele in partial_assignment[i] if ele]
            if len(row) != len(list(set(row))):
                return False
        return True # no dups in rows

    def check_dups_col():
        for i in range(9):
            col = [row[i] for row in partial_assignment if row[i]]
            if len(col) != len(list(set(col))):
                return False
        return True # no dups in cols

    def check_dups_sub_square():
        sub_square_centres = [[1 + i * 3, 1 + j * 3] for i in range(3) for j in range(3)]
        directions = [[i, j] for i in [-1, 0, 1] for j in [-1, 0, 1]]
        for center_x, center_y in sub_square_centres:
            coords = [[i + center_x, j + center_y] for i, j in directions]
            sub_square = [partial_assignment[x][y] for x, y in coords if partial_assignment[x][y]]
            if len(sub_square) != len(list(set(sub_square))):
                return False
        return True # no dups in sub squares

    no_dups_row = check_dups_row()
    no_dups_col = check_dups_col()
    no_dups_sub = check_dups_sub_square()

    return no_dups_row and no_dups_col and no_dups_sub

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
