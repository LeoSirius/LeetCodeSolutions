from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        m = len(matrix)
        n = len(matrix[0])
        pre = cur = [0 for i in range(n)]
        sz = 0
        for i in range(m):
            for j in range(n):
                if not i or not j or matrix[i][j] == '0':
                    cur[j] = int(matrix[i][j])
                else:
                    cur[j] = min(cur[j-1], pre[j], pre[j-1]) + 1
                sz = max(sz, cur[j])
            pre = cur
            cur = [0 for i in range(n)]
        return sz * sz


def test(test_name, matrix, expected):
    res = Solution().maximalSquare(matrix)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == "__main__":
    matrix1 = [
        ['1', '0', '1', '0', '0'],
        ['1', '0', '1', '1', '1'],
        ['1', '1', '1', '1', '1'],
        ['1', '0', '0', '1', '0'],
    ]
    expected1 = 4
    test('test1', matrix1, expected1)

    matrix2 = [['1']]
    expected2 = 1
    test('test2', matrix2, expected2)

    matrix3 = [["0","1"]]
    expected3 = 1
    test('test3', matrix3, expected3)

    matrix4 = []
    expected4 = 0
    test('test4', matrix4, expected4)