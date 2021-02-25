from typing import *


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        x, y = len(matrix), len(matrix[0])
        res = [[0] * x for _ in range(y)]

        for i in range(x):
            for j in range(y):
                res[j][i] = matrix[i][j]

        return res


def test(test_name, matrix, expected):
    res = Solution().transpose(matrix)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
    expected1 = [[1,4,7],[2,5,8],[3,6,9]]
    test('test1', matrix1, expected1)

    matrix2 = [[1,2,3],[4,5,6]]
    expected2 = [[1,4],[2,5],[3,6]]
    test('test2', matrix2, expected2)

