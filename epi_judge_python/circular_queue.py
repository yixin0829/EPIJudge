from test_framework import generic_test
from test_framework.test_failure import TestFailure

SCALE_FACTOR = 2


class Queue:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.queue = [0] * capacity
        self.head = self.tail = self.q_len = 0
        return

    def enqueue(self, x: int) -> None:
        if self.q_len == self.capacity:
            new_queue = [0] * self.capacity * SCALE_FACTOR
            for i in range(self.capacity):
                new_queue[i] = self.queue[(self.head + i) % self.capacity]
            # enqueue the new element and replace the old queue
            new_queue[self.capacity] = x
            self.queue = new_queue
            # reset head, tail, and capacity
            self.head, self.tail, self.capacity = 0, self.capacity, self.capacity * SCALE_FACTOR
        self.queue[self.tail % self.capacity] = x
        self.tail += 1
        self.q_len += 1
        return

    def dequeue(self) -> int:
        result, self.queue[self.head % self.capacity] = self.queue[self.head % self.capacity], 0
        self.head += 1
        self.q_len -= 1
        return result

    def size(self) -> int:
        return self.q_len


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure('Dequeue: expected ' + str(arg) + ', got ' +
                                  str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure('Size: expected ' + str(arg) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unsupported queue operation: ' + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('circular_queue.py',
                                       'circular_queue.tsv', queue_tester))
