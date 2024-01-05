from test_framework import generic_test
from test_framework.test_failure import TestFailure
from collections import OrderedDict

class LruCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache = OrderedDict()

    def lookup(self, isbn: int) -> int:
        if isbn not in self.cache:
            return -1
        result = self.cache[isbn]
        self.cache.move_to_end(isbn)
        return result

    def insert(self, isbn: int, price: int) -> None:
        if isbn in self.cache:
            # update ISBN to be the most recently w/o updating price
            self.cache.move_to_end(isbn)
        else:
            self.cache[isbn] = price

        if len(self.cache) > self.capacity:
            # pop the lru item at the front
            self.cache.popitem(last=False)
        return

    def erase(self, isbn: int) -> bool:
        if isbn in self.cache:
            del self.cache[isbn]
            return True
        else:
            return False


def lru_cache_tester(commands):
    if len(commands) < 1 or commands[0][0] != 'LruCache':
        raise RuntimeError('Expected LruCache as first command')

    cache = LruCache(commands[0][1])

    for cmd in commands[1:]:
        if cmd[0] == 'lookup':
            result = cache.lookup(cmd[1])
            if result != cmd[2]:
                raise TestFailure('Lookup: expected ' + str(cmd[2]) +
                                  ', got ' + str(result))
        elif cmd[0] == 'insert':
            cache.insert(cmd[1], cmd[2])
        elif cmd[0] == 'erase':
            result = 1 if cache.erase(cmd[1]) else 0
            if result != cmd[2]:
                raise TestFailure('Erase: expected ' + str(cmd[2]) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unexpected command ' + cmd[0])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lru_cache.py', 'lru_cache.tsv',
                                       lru_cache_tester))
