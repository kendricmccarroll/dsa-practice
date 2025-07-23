from typing import List

from test_framework import generic_test


def search_first_of_k(A: List[int], k: int) -> int:
    # TODO - you fill in here.

    l=0
    r=len(A)-1
    mid=0
    result = -1

    while l<=r:
        mid = (l+r) // 2

        if A[mid] > k:
            r = mid - 1
        elif A[mid] == k:
            result = mid
            r = mid -1
        elif A[mid] < k:
            l = mid + 1

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
