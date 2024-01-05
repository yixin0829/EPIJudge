import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
def reverse_words(s: list[str]):
    # TODO - you fill in here.
    # 1st pass to reverse individual word in the list
    # [mar si yltsoc]
    start = 0
    for i in range(len(s)):
        if s[i] == ' ':
            s[start: i] = reversed(s[start: i])
            start = i + 1 # assume only one whitespace between words

        # end of the last word
        if i == len(s) - 1:
            s[start: i + 1] = reversed(s[start: i + 1])

    # 2nd pass to reverse the whole string
    # [costly is ram]
    s.reverse()
    return s


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return ''.join(s_copy)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_words.py', 'reverse_words.tsv',
                                       reverse_words_wrapper))
