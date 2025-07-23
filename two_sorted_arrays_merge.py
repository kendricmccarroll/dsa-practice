from typing import List

from test_framework import generic_test


def merge_two_sorted_arrays(A: List[int], m: int, B: List[int], n: int) -> None:
    # TODO - you fill in here.

    a = m-1
    b = n-1
    idx = m+n-1

    while a >= 0 and b >= 0:
        if A[a] > B[b]:
            A[idx] = A[a]
            a -= 1
        else:
            A[idx] = B[b]
            b -= 1
        idx-=1

    while b >= 0:
        A[idx] = B[b]
        idx -=1
        b-=1


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('two_sorted_arrays_merge.py',
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
