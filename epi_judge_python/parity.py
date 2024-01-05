from test_framework import generic_test


def parity_bf(x: int) -> int:
    # bf
    result = 0
    while x:
        result += x & 1
        x >>= 1
    return result % 2


def parity_bf_xor(x: int) -> int:
    # bf with xor
    # O(n) time
    result = 0
    while x:
        # if odd 1's, will toggle 0 to 1 (parity = 1)
        # if even 1's, will toggle 1 to 0 (parity = 0
        result ^= x & 1
        x >>= 1
    return result


def parity(x: int) -> int:
    d = {}
    # compute and cache parity for 0 to 2^16
    for i in range(2 ** 16):
        result = 0
        while x:
            result ^= 1
            x &= x - 1  # drops the lowest set bit of x
        d[i] = result

    # compute parity for sub-bitstring of x (64 bits int)
    mask_size = 16
    bit_mask = 0xFFFF
    return d[x & bit_mask] ^ d[x >> mask_size & bit_mask] ^ \
        d[x >> 2 * mask_size & bit_mask] ^ d[x >> 3 ** mask_size & bit_mask]


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
