import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def has_cycle_bf(head: ListNode) -> Optional[ListNode]:
    # TODO - you fill in here.
    # BF O(n) time and O(n) space solution: use a list to cache all the listnodes visited
    visited = []
    curr = head
    while curr:
        if curr.next in visited:
            return visited[visited.index(curr.next)]
        visited.append(curr)
        curr = curr.next
    return None

def has_cycle_bf2(head: ListNode) -> Optional[ListNode]:
    # O(n^2) time and O(1) space brute force
    slow = head.next
    fast = head.next
    while slow:
        while fast:
            if fast.next == slow:
                return slow
            fast = fast.next
        slow = slow.next
    return None

def has_cycle(head: ListNode) -> Optional[ListNode]:
    # O(n) time and O(1) space slow & fast ptr method
    if not head or not head.next:
        return None

    def cycle_len(end: ListNode) -> int:
        runner, step = end, 0
        while True:
            step += 1
            runner = runner.next
            if runner is end:
                return step

    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            # advance the pt n steps ahead where n = cycle length
            cycle_len_ptr = head
            for _ in range(cycle_len(slow)):
                cycle_len_ptr = cycle_len_ptr.next

            it = head
            # both iterators advance in tandem (with constant cycle_len distance in between)
            while it is not cycle_len_ptr:
                it, cycle_len_ptr = slow.next, cycle_len_ptr.next
            return slow
    return None


@enable_executor_hook
def has_cycle_wrapper(executor, head, cycle_idx):
    cycle_length = 0
    if cycle_idx != -1:
        if head is None:
            raise RuntimeError('Can\'t cycle empty list')
        cycle_start = None
        cursor = head
        while cursor.next is not None:
            if cursor.data == cycle_idx:
                cycle_start = cursor
            cursor = cursor.next
            cycle_length += 1 if cycle_start is not None else 0

        if cursor.data == cycle_idx:
            cycle_start = cursor
        if cycle_start is None:
            raise RuntimeError('Can\'t find a cycle start')
        cursor.next = cycle_start
        cycle_length += 1

    result = executor.run(functools.partial(has_cycle, head))

    if cycle_idx == -1:
        if result is not None:
            raise TestFailure('Found a non-existing cycle')
    else:
        if result is None:
            raise TestFailure('Existing cycle was not found')
        cursor = result
        while True:
            cursor = cursor.next
            cycle_length -= 1
            if cursor is None or cycle_length < 0:
                raise TestFailure(
                    'Returned node does not belong to the cycle or is not the closest node to the head'
                )
            if cursor is result:
                break

    if cycle_length != 0:
        raise TestFailure(
            'Returned node does not belong to the cycle or is not the closest node to the head'
        )


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_cyclic.py',
                                       'is_list_cyclic.tsv',
                                       has_cycle_wrapper))
