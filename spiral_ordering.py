from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    # TODO - you fill in here.

    side = len(square_matrix) # 4
    start_row = 0
    ret = []

    if len(square_matrix) == 0:
        return []
    if len(square_matrix) == 1:
        ret.append(square_matrix[0][0])
        return ret

    while side > 0:
        for x in range(start_row, side-1):
            ret.append(square_matrix[start_row][x])

        for x in range(start_row, side-1):
            ret.append(square_matrix[x][side-1])

        for x in range(start_row, side-1):
            ret.append(square_matrix[side-1][side-x-1])

        for x in range(start_row, side-1):
            ret.append(square_matrix[side-x-1][start_row])

        side -= 2
        start_row += 1

    z = len(square_matrix)

    if z//2 == 1:
        ret.append(square_matrix[z-1//2][z-1//2])

    return ret


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
