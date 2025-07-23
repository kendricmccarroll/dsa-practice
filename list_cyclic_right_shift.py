from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def cyclically_right_shift_list(L: ListNode, k: int) -> Optional[ListNode]:
    # TODO - you fill in here.


    dummyhead = dummyhead2 = newhead = L
    length=0
    while dummyhead:
        dummyhead=dummyhead.next
        length+=1

    k = k % length
    start = length-k-1

    count = 0
    while count < start:
        dummyhead2 = dummyhead2.next

    newhead = dummyhead2
    tmp = dummyhead2.next
    dummyhead2.next = None
    dummyhead.next = tmp
    return newhead





    return None


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('list_cyclic_right_shift.py',
                                       'list_cyclic_right_shift.tsv',
                                       cyclically_right_shift_list))
