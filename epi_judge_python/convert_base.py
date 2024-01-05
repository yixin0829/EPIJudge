from test_framework import generic_test


# a variant of 6.1 string_integer_interconversion
def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    # TODO - you fill in here.
    # convert b1 to base-10 and then to b2
    # O(2n) time and O(n) space
    neg = False
    if num_as_string == '':
        return ''
    elif num_as_string == '0':
        return '0'
    elif num_as_string[0] == '-':
        neg, num_as_string = True, num_as_string[1:]

    result = [] # store base-b2 num as separate char digits

    # convert b1 string to base 10 int
    num_b10 = 0
    for c in num_as_string:
        num_b10 = num_b10 * b1 + int(c, b1) # NOTE: int(s, base) convert the string to base b1

    # convert base 10 int to b2 string
    while num_b10 > 0:
        result.append(hex(num_b10 % b2)[2:].upper()) # hex() return "0xa"
        num_b10 //= b2

    return ('-' if neg else '') + ''.join(reversed(result))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
