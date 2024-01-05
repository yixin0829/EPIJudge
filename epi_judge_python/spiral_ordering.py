from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    # TODO - you fill in here.
    # divide and conquer with recursion O(n^2) time where n = dim
    def traverse_outer_matrix(x, y, dim):
        # traverse the outer "shell" of the matrix cw
        # starting x, y coord + dimension the sub square
        if dim == 0:
            return []
        if dim == 1:
            return [square_matrix[x][y]]

        result = []
        # first row of the shell inclusive
        for i in range(dim):
            result.append(square_matrix[x][y + i])
        # last column downward '' exclude both ends
        for i in range(dim - 2):
            result.append(square_matrix[x + 1 + i][y + dim - 1])
        # last row '' inclusive
        for i in range(dim):
            result.append(square_matrix[x + dim - 1][y + dim - 1 - i])
        # first column upward '' exclude both ends
        for i in range(dim - 2):
            result.append(square_matrix[x + dim - 2 - i][y])
        return result

    dim_matrix = len(square_matrix)
    start_x, start_y = 0, 0
    ans = []
    while dim_matrix > 0:
        ans.extend(traverse_outer_matrix(start_x, start_y, dim_matrix))
        start_x += 1
        start_y += 1
        dim_matrix -= 2

    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
