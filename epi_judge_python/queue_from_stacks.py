from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    def __init__(self):
        self.enq_stack = []
        self.deq_stack = []

    def enqueue(self, x: int) -> None:
        # O(1)
        self.enq_stack.append(x)

    def dequeue(self) -> int:
        # O(m)
        if not self.deq_stack:
            while self.enq_stack:
                self.deq_stack.append(self.enq_stack.pop())
        return self.deq_stack.pop()


def queue_tester(ops):
    try:
        q = Queue()

        for (op, arg) in ops:
            if op == 'Queue':
                q = Queue()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure('Dequeue: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported queue operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('queue_from_stacks.py',
                                       'queue_from_stacks.tsv', queue_tester))
