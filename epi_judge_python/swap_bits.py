from test_framework import generic_test


def swap_bits(x, i, j):
    # read ith and jth bit
    i_bit = (x >> i) & 1
    j_bit = (x >> j) & 1

    if i_bit != j_bit:
        # instead of swapping the bits we simply toggle (flip) it using XOR O(1)

        # approach 1: toggle one by one
        # x = x ^ (1 << i)
        # x = x ^ (1 << j)

        # approach 2: construct a bit mask and do an XOR toggle at once
        bit_mask = (1 << i) | (1 << j)
        x ^= bit_mask

    return x

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
                                       swap_bits))
