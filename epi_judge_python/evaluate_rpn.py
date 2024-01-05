from test_framework import generic_test


def evaluate(expression: str) -> int:
    s = []  # stack to store intermediary evaluation result
    expression_list = expression.split(',')

    for c in expression_list:
        # if symbol then start evaluating and push the result to stack
        if c == '+':
            n2, n1 = s.pop(), s.pop()
            s.append(n1 + n2)
        elif c == '-':
            n2, n1 = s.pop(), s.pop()
            s.append(n1 - n2)
        elif c == '*':
            n2, n1 = s.pop(), s.pop()
            s.append(n1 * n2)
        elif c == '/':
            n2, n1 = s.pop(), s.pop()
            s.append(n1 // n2)
        else:
            s.append(int(c))

    return s[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
