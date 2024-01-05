from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    # TODO - you fill in here.
    result = []
    neg = True if x < 0 else False
    x = -x if neg else x

    while x > 0:
        result.append(str(x % 10))
        x //= 10

    if neg:
        result.append("-")

    return "".join(result[::-1])


def string_to_int(s: str) -> int:
    # TODO - you fill in here.
    result = 0
    neg = True if s[0] == "-" else False
    # turn "-123" or "+123" to "123"
    if s[0] in ["-", "+"]:
        s = s[1:]

    for c in s:
        result = result * 10 + ord(c) - ord("0")

    return -result if neg else result


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
