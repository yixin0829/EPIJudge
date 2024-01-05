from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    # O(n) space and O(1) time
    if L is None: # empty 1st node = empty list
        return None

    # trick use two dummy heads to track two list and reuse nodes to save space
    dummy_even_tail, dummy_odd_tail = ListNode(0), ListNode(0)
    tails, turn = [dummy_even_tail, dummy_odd_tail], 0

    while L:
        tails[turn].next = L
        L = L.next
        tails[turn] = tails[turn].next
        turn ^= 1  # XOR toggle

    tails[1].next = None
    tails[0].next = dummy_odd_tail.next

    return dummy_even_tail.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
