import collections
import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_smallest_subarray_covering_set_bf(paragraph: List[str],
                                        keywords: Set[str]) -> Subarray:
    # O(n ^ 3) time brute force solution
    smallest_subarray = Subarray(0, 10000)
    for i in range(len(paragraph)):
        for j in range(i, len(paragraph)):

            if keywords <= set(paragraph[i:j+1]):
                if (j - i) < (smallest_subarray.end - smallest_subarray.start):
                    smallest_subarray = Subarray(i, j)

    return smallest_subarray

def find_smallest_subarray_covering_set(paragraph: List[str],
                                           keywords: Set[str]) -> Subarray:
    # O(n) two pointer solution -> see solution revisit later
    return Subarray(-1, -1)

@enable_executor_hook
def find_smallest_subarray_covering_set_wrapper(executor, paragraph, keywords):
    copy = keywords

    (start, end) = executor.run(
        functools.partial(find_smallest_subarray_covering_set, paragraph,
                          keywords))

    if (start < 0 or start >= len(paragraph) or end < 0
            or end >= len(paragraph) or start > end):
        raise TestFailure('Index out of range')

    for i in range(start, end + 1):
        copy.discard(paragraph[i])

    if copy:
        raise TestFailure('Not all keywords are in the range')

    return end - start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'smallest_subarray_covering_set.py',
            'smallest_subarray_covering_set.tsv',
            find_smallest_subarray_covering_set_wrapper))
