from list_node import ListNode
from test_framework import generic_test


def reverse_list_solution(head: ListNode) -> ListNode:
    dummy = ListNode(0)
    while head:
        dummy.next, head.next, head = head, dummy.next, head.next
    return dummy.next

# Yixin's iterative implementation
def reverse_list(head: ListNode) -> ListNode:
    dummy = ListNode(0)
    while head:
        temp_next = head.next # save current next
        head.next = dummy.next # set current next to prev (i.e. dummy.next)
        dummy.next = head # advance prev
        head = temp_next # advance current
    return dummy.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_list.py', 'reverse_list.tsv',
                                       reverse_list))
