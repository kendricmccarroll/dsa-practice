from typing import List

from test_framework import generic_test


def search_smallest(A: List[int]) -> int:
    # TODO - you fill in here.

    l=0
    r=len(A)-1

    return 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_shifted_sorted_array.py',
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
