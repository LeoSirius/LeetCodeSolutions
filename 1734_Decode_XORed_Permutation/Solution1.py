from typing import *

class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        res1, res2 = 0, 0
        n = len(encoded) + 1
        perm = [0] * n

        for i, v in enumerate(encoded):
            if i % 2 == 0:
                res1 ^= v

        for i in range(1, n + 1):
            res2 ^= i

        perm[-1] = res1 ^ res2
        for i in range(n-2, -1, -1):
            perm[i] = perm[i+1] ^ encoded[i]

        return perm


def test(test_name, encoded, expected):
    res = Solution().decode(encoded)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    encoded1 = [3,1]
    expected1 = [1,2,3]
    test('test1', encoded1, expected1)

    encoded2 = [6,5,4,6]
    expected2 = [2,4,1,5,3]
    test('test2', encoded2, expected2)
