from test_framework import generic_test


def is_well_formed(s: str) -> bool:
    # e.g. "[()()]" is a well-formed string
    stack = []  # init a stack
    mapping = {'[': ']', '(': ')', '{': '}'}

    for c in s:
        if c in ['[', '(', '{']:
            # it's left parentheses push it in stack
            stack.append(c)
        else:
            # it's right parentheses pop from stack
            if stack and mapping[stack.pop()] == c:
                continue
            else:
                return False

    return len(stack) == 0  # return True if stack is empty


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
