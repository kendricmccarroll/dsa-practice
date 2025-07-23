from test_framework import generic_test


def can_form_palindrome(s: str) -> bool:
    # TODO - you fill in here.

    d = {}
    for x in s:
        if x.isalpha():
            if not d.get(x):
                d[x] = 1
            else:
                d[x] += 1

    oneOdd = 0;

    for x in d:
        if d[x] % 2 == 0:
            continue
        else:
            oneOdd+=1
            if oneOdd > 1:
                return False

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_permutable_to_palindrome.py',
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
