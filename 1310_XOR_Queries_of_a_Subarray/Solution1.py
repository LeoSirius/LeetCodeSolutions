from typing import *
from itertools import accumulate
from operator import xor

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prexor = list(accumulate([0] + arr, xor))
        return [prexor[l] ^ prexor[r+1] for l, r in queries]


def test(test_name, arr, queries, expected):
    res = Solution().xorQueries(arr, queries)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    arr1 = [1,3,4,8]
    queries1 = [[0,1],[1,2],[0,3],[3,3]]
    expected1 = [2,7,14,8]
    test('test1', arr1, queries1, expected1)

    arr2 = [4,8,2,10]
    queries2 = [[2,3],[1,3],[0,0],[0,3]]
    expected2 = [8,0,4,4]
    test('test2', arr2, queries2, expected2)
