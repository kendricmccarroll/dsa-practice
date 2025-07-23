import heapq
from typing import Iterator, List

from test_framework import generic_test


def sort_approximately_sorted_array(sequence: Iterator[int], k: int) -> List[int]:


    min_heap: List[int] = []
    ret=[]

    for x in range(0,k):
        min_heap.append(next(sequence))

    print(min_heap)

    heapq.heapify(min_heap)

    print(min_heap)

    for x in sequence:
        heapq.heappush(min_heap, x)
        small=heapq.heappop(min_heap)

        ret.append(small)


    while min_heap:
        smallest = heapq.heappop(min_heap)
        ret.append(smallest)

    return ret



def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'sort_almost_sorted_array.py', 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
