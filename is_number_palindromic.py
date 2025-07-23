from test_framework import generic_test


def is_palindrome_number(x: int) -> bool:
    # TODO - you fill in here.

    stack=[]
    if x < 0:
        return False
    elif x < 10:
        return True
    else:
        while x:
            stack.append(str(x % 10))
            x //= 10

    l = 0
    r = len(stack)-1

    while l<r:
        if stack[l] != stack[r]:
            return False
        else:
            l += 1
            r -= 1


    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
