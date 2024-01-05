from test_framework import generic_test


def look_and_say(n: int) -> str:
    def map_to_pairs(s):
        """
        Given "1122"
        Return [['2', '1'], ['2', '2']]
        """
        result = []
        counter = [0, s[0]]  # count, num_str
        for i, c in enumerate(s):
            if c == counter[1]:
                counter[0] += 1
            else:
                counter[0] = str(counter[0])
                result.append(counter)
                counter = [1, c]  # reset counter

        # push the last digit seq pair e.g. '111223' last pair is [1, '3']
        counter[0] = str(counter[0])
        result.append(counter)
        return result

    ans = []
    if n == 1:
        return '1'
    else:
        last_seq = look_and_say(n - 1)
        pairs = map_to_pairs(last_seq)
        for p in pairs:
            ans.extend(p)

    return ''.join(ans)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))
