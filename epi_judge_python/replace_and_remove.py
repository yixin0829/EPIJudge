import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove_bf(size: int, s: List[str]) -> int:
    # TODO - you fill in here.
    # O(n) time and O(n) space brute force
    result = []
    for i in range(size):
        if s[i] == 'a':
            result.extend(['d'] * 2)
        elif s[i] == 'b':
            continue
        else:
            result.append(s[i])

    s[:len(result)] = result # O(1)

    return len(result)

def replace_and_remove(size: int, s: List[str]) -> int:
    # O(2n) time and O(1) space

    # forward pass to count num of 'a' while removing 'b'
    a_count, write_idx = 0, 0

    for i in range(size):
        if s[i] != 'b':
            s[write_idx] = s[i]
            write_idx += 1
        if s[i] == 'a':
            a_count += 1

    # calculate the final array length
    cur_idx = write_idx - 1
    write_idx += a_count - 1
    final_size = write_idx + 1

    # backward pass to replace 'a' with 'dd'
    while cur_idx >= 0:
        if s[cur_idx] == 'a':
            s[write_idx - 1: write_idx + 1] = 'dd'
            write_idx -= 2
        else:
            s[write_idx] = s[cur_idx]
            write_idx -= 1
        cur_idx -= 1
    return final_size

@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
