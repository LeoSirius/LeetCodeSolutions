from typing import *
from heapq import *

class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n+1) for _ in range(m+1)]
        hp = [0] * k
        heapify(hp)

        for i in range(m):
            for j in range(n):
                cur_xor = dp[i][j] ^ dp[i+1][j] ^ dp[i][j+1] ^ matrix[i][j]
                dp[i+1][j+1] = cur_xor

                if cur_xor > hp[0]:
                    heappop(hp)
                    heappush(hp, cur_xor)
        return hp[0]


def test(test_name, matrix, k, expected):
    res = Solution().kthLargestValue(matrix, k)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    matrix1 = [[5,2],[1,6]]
    k1 = 1
    expected1 = 7
    test('test1', matrix1, k1, expected1)

    matrix2 = [[5,2],[1,6]]
    k2 = 2
    expected2 = 5
    test('test2', matrix2, k2, expected2)

    matrix3 = [[5,2],[1,6]]
    k3 = 3
    expected3 = 4
    test('test3', matrix3, k3, expected3)

    matrix4 = [[5,2],[1,6]]
    k4 = 4
    expected4 = 0
    test('test4', matrix4, k4, expected4)

    matrix5 = [[8,10,5,8,5,7,6,0,1,4,10,6,4,3,6,8,7,9,4,2]]
    k5 = 2
    expected5 = 14
    test('test5', matrix5, k5, expected5)
