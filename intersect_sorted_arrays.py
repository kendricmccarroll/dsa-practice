from typing import List

from test_framework import generic_test


def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    # TODO - you fill in here.

    if len(A) ==0:
        return []
    if len(B) == 0:
        return []

    # ret = []
    # start = min(A[0], B[0])
    #
    # for x in A:
    #     if x in B and x not in ret:
    #         ret.append(x)

    i,j,ret = 0,0,[]
    while i<len(A) and j<len(B):
        if A[i] == B[j]:
            if i == 0 or A[i] != A[i-1]:
                ret.append(A[i])
            i+=1
            j+=1
        elif A[i] > B[j]:
            j+=1
        else:
            i+=1




    return ret


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
