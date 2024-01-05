import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_lists(l0: ListNode, l1: ListNode) -> Optional[ListNode]:
    # TODO - you fill in here.
    def length(L):
        length = 0
        while L:
            length += 1
            L = L.next
        return length

    # 1st and 2nd pass
    len0, len1 = length(l0), length(l1)
    if len0 > len1:
        l0, l1 = l1, l0 # l1 is the longer list

    # 3rd pass to find the first overlapped node
    # advance the loger list to get equal length lists
    for _ in range(abs(len0 - len1)):
        l1 = l1.next

    while l0 and l1 and l0 is not l1:
        l0, l1 = l0.next, l1.next

    return l0 # None will be returned if there's no overlap


@enable_executor_hook
def overlapping_lists_wrapper(executor, l0, l1, common, cycle0, cycle1):
    if common:
        if not l0:
            l0 = common
        else:
            it = l0
            while it.next:
                it = it.next
            it.next = common

        if not l1:
            l1 = common
        else:
            it = l1
            while it.next:
                it = it.next
            it.next = common

    if cycle0 != -1 and l0:
        last = l0
        while last.next:
            last = last.next
        it = l0
        for _ in range(cycle0):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    if cycle1 != -1 and l1:
        last = l1
        while last.next:
            last = last.next
        it = l1
        for _ in range(cycle1):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    common_nodes = set()
    it = common
    while it and id(it) not in common_nodes:
        common_nodes.add(id(it))
        it = it.next

    result = executor.run(functools.partial(overlapping_lists, l0, l1))

    if not (id(result) in common_nodes or (not common_nodes and not result)):
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_lists_overlap.py',
                                       'do_lists_overlap.tsv',
                                       overlapping_lists_wrapper))
