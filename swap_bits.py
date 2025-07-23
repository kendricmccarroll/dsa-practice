from test_framework import generic_test


def swap_bits(x, i, j):

    left = 1 & x >> i
    right = 1 & x >> j

    print("left :" + str(left))
    print("right: " + str(right))

    if (x >> i) &1 != (x >> j) & 1:
        mask = (1 << i) | (1 << j)
        x=x^mask

    return x

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
                                       swap_bits))
