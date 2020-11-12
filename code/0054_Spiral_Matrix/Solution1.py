from typing import *

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not matrix:
            return res

        m, n = len(matrix), len(matrix[0])
        left, right, top, bottom = 0, n-1, 0, m-1

        while left <= right and top <= bottom:
            for i in range(left, right+1):
                res.append(matrix[top][i])
            top += 1

            for i in range(top, bottom+1):
                res.append(matrix[i][right])
            right -= 1

            # 最后两个要一起判断，不然会有重复
            # [left, right], [top, bottom]中只要有一个相等，就说明都走过了
            if left <= right and top <= bottom:
                for i in range(right, left-1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1

                for i in range(bottom, top-1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res


def test(test_name, matrix, expected):
    res = Solution().spiralOrder(matrix)
    if res == expected:
        print(f'{test_name} success.')
    else:
        print(f'{test_name} failed.')


if __name__ == "__main__":
    matrix1 = [
        [ 1, 2, 3 ],
        [ 4, 5, 6 ],
        [ 7, 8, 9 ]
    ]
    expected1 = [1,2,3,6,9,8,7,4,5]
    test('test1', matrix1, expected1)

    matrix2 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9,10,11,12]
    ]
    expected2 = [1,2,3,4,8,12,11,10,9,5,6,7]
    test('test2', matrix2, expected2)


# Given a matrix of m x n elements (m rows, n columns), return
#  all elements of the matrix in spiral order.

# Example 1:

# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:

# Input:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

