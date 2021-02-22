from typing import *


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] != matrix[i-1][j-1]:
                    return False
        return True


def test(test_name, matrix, expected):
    res = Solution().isToeplitzMatrix(matrix)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    matrix1 = [
        [1,2,3,4],
        [5,1,2,3],
        [9,5,1,2]]
    expected1 = True
    test('test1', matrix1, expected1)

    matrix2 = [
        [1,2],
        [2,2]]
    expected2 = False
    test('test2', matrix2, expected2)

