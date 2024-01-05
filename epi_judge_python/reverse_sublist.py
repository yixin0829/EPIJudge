from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    # TODO - you fill in here.
    if not L or not L.next:
        return L

    # advance to node before start (if start is 1 then no advance needed)
    head = tail = None # node before start and node after finish
    curr = L
    count = 0
    while curr:
        if count == (start - 1):
            head = curr
        elif count == finish:
            tail = curr
        count += 1
        curr = curr.next

    dummy = ListNode(0, tail)
    curr = head.next  # node at start
    while curr != tail:
        temp_next = curr.next
        curr.next = dummy.next
        dummy.next = curr
        curr = temp_next

    head.next = dummy.next
    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
