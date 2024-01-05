from test_framework import generic_test


def reverse_bits_bf(x: int) -> int:
    # BF: O(n) time and O(1) space
    for i in range(32): # O(n/2)
        # matching bit for the first 32 bit (0 matches 63, 1 matches 62, ...)
        j = 63 - i

        # swap bit j and bit i
        if (x >> j) & 1 != (x >> i) & 1: # O(1)
            # toggle bit is equivalent to swapping
            bit_mask = (1 << j) | (1 << i)
            x ^= bit_mask
    return x

def reverse_bits(x: int) -> int:
    # use a hash map to cache precomputed reversed bits for 16-bit sub-sequence
    # since we only need to cache 16-bit reversed bits (~60000 entries) once can ignore it in time complexity

    # O(n/L) time where L = 16
    # see solution
    pass

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
