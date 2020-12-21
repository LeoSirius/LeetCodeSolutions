from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

def test(test_name, matrix, expected):
    Solution().rotate(matrix)
    if matrix == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    matrix1 = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    expected1 = [
        [7,4,1],
        [8,5,2],
        [9,6,3]
    ]
    test('test1', matrix1, expected1)

    matrix2 = [
        [ 5, 1, 9,11],
        [ 2, 4, 8,10],
        [13, 3, 6, 7],
        [15,14,12,16]
    ]
    expected2 = [
        [15,13, 2, 5],
        [14, 3, 4, 1],
        [12, 6, 8, 9],
        [16, 7,10,11]
    ]
    test('test2', matrix2, expected2)
