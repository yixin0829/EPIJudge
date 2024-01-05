from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    # TODO - you fill in here.

    # increment from the back
    A[-1] += 1
    # loop the array reversely
    for i in range(len(A) - 1, -1, -1):
        if A[i] == 10 and i: # i is not at 0 index
            A[i] = 0
            A[i-1] += 1
        elif A[i] == 10 and not i: # i is at 0 index (e.g. [9, 9] or [9])
            A[i] = 1
            A.extend([0 * len(A)]) # see the solution for a slick O(1) way to do this
        else:
            break

    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
