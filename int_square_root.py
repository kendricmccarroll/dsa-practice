from test_framework import generic_test


def square_root(k: int) -> int:
    # TODO - you fill in here.


    l=0
    r=k

    while l <= r:
        m = (l+r) // 2
        mid_s = m * m
        if mid_s  <= k:
            l = m +1
        else:
            r = m -1

    return l-1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
