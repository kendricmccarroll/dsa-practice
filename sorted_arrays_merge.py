import heapq
from typing import List

from test_framework import generic_test


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:

    L=[]
    ret = []

    for x in sorted_arrays:
        L.append(x[0])

    heapq.heapify(L)
    while L:
        ret.append(heapq.heappop())


    # TODO - you fill in here.


    return []


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
