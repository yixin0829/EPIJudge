import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook
from collections import Counter


# Returns the number of valid entries after deletion.
def delete_duplicates(A: List[int]):
    # TODO - you fill in here.
    # two-pointer approach. one slow pointer that points to the position to be write another new value
    # a fast pointer to loop through the array to check duplicates
    # O(n) time and O(1) space
    if not A:
        return 0

    slow = 0
    for fast in range(1, len(A)):
        if A[slow] != A[fast]:
            A[slow + 1] = A[fast]
            slow += 1
    return slow + 1

@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('delete_dups_from_sorted_array.py',
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
