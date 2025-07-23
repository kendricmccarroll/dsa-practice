from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    # TODO - you fill in here.
    neg = False;
    if x < 0:
        neg = True
        x = x*-1
    s = []
    while x:
        s.append(chr(ord('0') + x % 10) )
        x = x//10

    if neg:
        s.append('-')
    return "".join(reversed(s))


def string_to_int(s: str) -> int:

    neg = False;
    start = 0
    ret =0
    mul = 1

    if s[0] == "-":
        neg==True
        start = 1
    if s[0] == '+':
        start =1


    for l in s[start:len(s)-1:-1]:
        ret += mul*int(l)
        mul = 10*mul





    # TODO - you fill in here.
    return 0


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
