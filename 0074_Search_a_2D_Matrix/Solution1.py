from typing import *

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i, j = 0, len(matrix[0]) - 1

        while i < len(matrix) and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1

        return False


def test(test_name, matrix, target, expected):
    res = Solution().searchMatrix(matrix, target)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    matrix1 = [
        [1, 3, 5, 7],
        [10,11,16,20],
        [23,30,34,60]]
    target1 = 3
    expected1 = True
    test('test1', matrix1, target1, expected1)

    matrix2 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target2 = 13
    expected2 = False
    test('test2', matrix2, target2, expected2)
