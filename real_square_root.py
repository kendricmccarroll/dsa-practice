import math

from test_framework import generic_test


def square_root(x: float) -> float:
    # TODO - you fill in here.

    if x < 1:
        l=0
        r=1
    else:
        l = 0
        r = x

    while not math.isclose(l, r):

        m = (l+r) * .5
        ms = m *m
        if ms > x:
            r = m
        else:
            l = m


    return l

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('real_square_root.py',
                                       'real_square_root.tsv', square_root))
