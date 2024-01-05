from typing import List

from math import sqrt
from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes_bf(n: int) -> List[int]:
    # Brute force - O(n^(3/2)) time and O(n) space
    if n == 1:
        return []

    # takes O(n^(1/2)) time to check if a number is prime by "trial and division" method
    def is_prime(number: int) -> bool:
        for i in range(2, int(sqrt(number))):
            if number % i == 0:
                return False
        return True

    result = []
    is_prime_lis = [False, False] + [True] * (n-1)
    for num in range(2, n+1):
        # check if it's a multiple of prime or even number
        if (num % 2 == 0 and num != 2) or not is_prime_lis[num]:
            continue

        if is_prime(num):
            result.append(num)
            # set all prime's multiples to False
            for i in range(num * 2, n + 1, num):
                is_prime_lis[i] = False

    return result


def generate_primes(n: int) -> List[int]:
    result = []
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('enumerate_all_prime_to_n.py', 'prime_sieve.tsv',
                                       generate_primes_bf))
