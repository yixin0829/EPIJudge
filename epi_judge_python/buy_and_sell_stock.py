from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once_bf(prices: List[float]) -> float:
    # TODO - you fill in here.
    # BF - O(n^2) time and O(1) space
    # compute all possible profits and keep track of the highest one
    highest = 0.0
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[j] - prices[i] > highest:
                highest = prices[j] - prices[i]

    return highest

def buy_and_sell_stock_once(prices: List[float]) -> float:
    # O(n) one pass: realize that the max profit we can make at each day is (current price - lowest seen so far)
    # this is a simple memoization used in DP. here our cache is lowest_so_far
    max_profit, lowest_so_far = 0.0, float("inf")
    for i in range(len(prices)):
        profit = prices[i] - lowest_so_far
        lowest_so_far = min(lowest_so_far, prices[i])
        max_profit = max(max_profit, profit)

    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
