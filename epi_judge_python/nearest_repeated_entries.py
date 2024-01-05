from typing import List

from test_framework import generic_test


def find_nearest_repetition(paragraph: List[str]) -> int:
    # O(n) time and O(n) space

    word_to_latest_idx = {}
    nearest_dist = float('inf')
    for i, word in enumerate(paragraph):
        if word in word_to_latest_idx:
            latest_equal_word = word_to_latest_idx[word]
            nearest_dist = min(nearest_dist,
                               i - latest_equal_word)
        word_to_latest_idx[word] = i
    return int(nearest_dist) if nearest_dist != float('inf') else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
