from typing import *
from collections import defaultdict


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        presum = [[0] * (n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                presum[i][j] = presum[i-1][j] + presum[i][j-1] - presum[i-1][j-1] + matrix[i-1][j-1]
        res = 0
        for top in range(1, m+1):
            for bot in range(top, m+1):
                mp = defaultdict(int)
                for r in range(1, n+1):
                    cur = presum[bot][r] - presum[top-1][r]
                    if cur == target:
                        res += 1
                    n2find = cur - target
                    res += mp.get(n2find, 0)
                    mp[cur] += 1

        return res


def test(test_name, matrix, target, expected):
    res = Solution().numSubmatrixSumTarget(matrix, target)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    matrix1 = [[0,1,0],[1,1,1],[0,1,0]]
    target1 = 0
    expected1 = 4
    test('test1', matrix1, target1, expected1)

    matrix2 = [[1,-1],[-1,1]]
    target2 = 0
    expected2 = 5
    test('test2', matrix2, target2, expected2)

    matrix3 = [[904]]
    target3 = 0
    expected3 = 0
    test('test3', matrix3, target3, expected3)
