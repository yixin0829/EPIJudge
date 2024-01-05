from test_framework import generic_test


def power_bf(x: float, y: int) -> float:
    # BF: multiply x y times iteratively O(n) time and O(1) space

    # corner cases
    if y == 0 or x == 1:
        return 1
    elif x == 0:
        return 0

    neg_exp = True if y < 0 else False
    y = -y if neg_exp else y

    ans = 1
    for i in range(y):
        ans *= x

    return ans if not neg_exp else 1/ans


def power_recursive(x: float, y: int) -> float:
    # recursive O(logN) time and O(logY) space for call stack
    if y == 0:
        return 1
    elif y == 1:
        return x

    neg_exp = True if y < 0 else False
    y = -y if neg_exp else y

    ans = None
    # if y is odd number, minus 1
    if y % 2:
        y -= 1
        ans = x * pow(x, y // 2) * pow(x, y // 2)
    else:
        ans = pow(x, y // 2) * pow(x, y // 2)

    return 1/ans if neg_exp else ans


def power(x: float, y: int) -> float:
    # bits manipulation (fastest)
    result, power = 1.0, y
    if y < 0:
        power, x = -power, 1.0 / x

    while power:
        if power & 1:
            result *= x
        x = x * x
        power >>= 1

    return result


if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
