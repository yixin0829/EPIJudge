import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

def even_odd_bf(A: List[int]) -> None:
    # bf: O(n) time and O(n) space. Most array problems are easy with O(n) space
    even = []
    odd = []
    for num in A:
        if num % 2:
            # operate efficiently on the back of array O(1) insertion if resizing is by a factor (e.g. 2)
            odd.append(num)
        else:
            even.append(num)
    return even + odd

def even_odd(A: List[int]) -> None:
    # use two pointers to determine the boundaries b/w even & unclassified or unclassified & odd
    # partition the array (i.e. a list here) into three parts: even, unclassified, and odd
    # O(n) time and O(1) space
    left, right = 0, len(A) - 1
    while left < right:
        if A[left] % 2: # if odd then swap
            A[left], A[right] = A[right], A[left]
            right -= 1
        else:
            left += 1

    return A


@enable_executor_hook
def even_odd_wrapper(executor, A):
    before = collections.Counter(A)

    executor.run(functools.partial(even_odd, A))

    in_odd = False
    for a in A:
        if a % 2 == 0:
            if in_odd:
                raise TestFailure('Even elements appear in odd part')
        else:
            in_odd = True
    after = collections.Counter(A)
    if before != after:
        raise TestFailure('Elements mismatch')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_array.py',
                                       'even_odd_array.tsv', even_odd_wrapper))
