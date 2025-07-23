import math
from typing import List

from test_framework import generic_test


def find_nearest_repetition(paragraph: List[str]) -> int:
    # TODO - you fill in here.

    # d = dict[str, int]
    d = {}
    curr_min = float('inf')
    print(curr_min)

    for i, x in enumerate(paragraph):
        if x not in d:
            d[x] = i
        else:
            if i - d[x] < curr_min:
                curr_min = i - d[x]
            d[x] = i


    if curr_min == float('inf'):
        return -1
    else:
        return curr_min


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
