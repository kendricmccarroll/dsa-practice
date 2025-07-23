from typing import List

from test_framework import generic_test


def matrix_search(A: List[List[int]], x: int) -> bool:
    # TODO - you fill in here.

    if not A:
        return False

    l = 0
    r = len(A[0]) - 1
    for y in A:
        for z in A[y]:
            if x == z:
                return True
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_row_col_sorted_matrix.py',
                                       'search_row_col_sorted_matrix.tsv',
                                       matrix_search))
