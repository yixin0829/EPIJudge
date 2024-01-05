from test_framework import generic_test


def reverse_module(x: int) -> int:
    # using module % to get digits O(n) time and O(n) space where n is the num of digits in x
    # considering a 64-bit int have only 20 digits it's basically O(1) time and O(1) space
    neg = True if x < 0 else False
    x = -x if neg else x

    digits = []
    while x:
        # get the smallest digit
        smallest_digit = x % 10
        digits.append(smallest_digit)

        # update x
        x = (x - smallest_digit) / 10

    # construct a new reversed int from digits
    ans = 0
    for d in digits:
        ans = ans * 10 + d

    return -ans if neg else ans

def reverse(x: int) -> int:
    # solution: optimized with one while loop O(n) time and O(1) space
    ans, x_remaining = 0, abs(x)
    while x_remaining:
        ans = ans * 10 + x_remaining % 10
        x_remaining //= 10
    return -ans if x < 0 else ans

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
