from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Stack_bf:
    def __init__(self):
        self.s = []

    def empty(self) -> bool:
        # O(n)
        return len(self.s) == 0

    def max(self) -> int:
        # O(n)
        return max(self.s)

    def pop(self) -> int:
        # O(1)
        return self.s.pop()

    def push(self, x: int) -> None:
        # O(1)
        self.s.append(x)
        return


class Stack:
    def __init__(self):
        # a stack of tuple of (val, max at val)
        self.s: list[tuple] = []

    def empty(self) -> bool:
        # O(n)
        return len(self.s) == 0

    def max(self) -> int:
        # O(1) time with O(n) space cache
        return max(self.s[-1])

    def pop(self) -> int:
        # O(1)
        return self.s.pop()[0]  # recall tuple of (val, max at val)

    def push(self, x: int) -> None:
        # O(1)
        self.s.append((x, x if self.empty() else max(self.max(), x)))
        return


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure('Pop: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure('Empty: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported stack operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('stack_with_max.py',
                                       'stack_with_max.tsv', stack_tester))
