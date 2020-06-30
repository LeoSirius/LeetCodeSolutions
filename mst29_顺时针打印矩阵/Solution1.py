from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not matrix or not matrix[0]:
            return res

        rbegin, rend, cbegin, cend = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        while True:
            for i in range(cbegin, cend + 1): res.append(matrix[rbegin][i])
            rbegin += 1
            if rbegin > rend: break

            for i in range(rbegin, rend + 1): res.append(matrix[i][cend])
            cend -= 1
            if cbegin > cend: break

            for i in range(cend, cbegin-1, -1): res.append(matrix[rend][i])
            rend -= 1
            if rbegin > rend: break

            for i in range(rend, rbegin-1, -1): res.append(matrix[i][cbegin])
            cbegin += 1
            if cbegin > cend: break

        return res

def test(test_name, matrix, expected):
    res = Solution().spiralOrder(matrix)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == "__main__":
    matrix1 = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    expected1 = [1,2,3,6,9,8,7,4,5]
    test('test1', matrix1, expected1)

    matrix2 = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]
    ]
    expected2 = [1,2,3,4,8,12,11,10,9,5,6,7]
    test('test2', matrix2, expected2)

#  输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

#  限制：

#  0 <= matrix.length <= 100
#  0 <= matrix[i].length <= 100
