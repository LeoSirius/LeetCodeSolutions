from typing import *

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:

        def get_sum(i, j, m, n):
            res = 0

            for x in range(i, m+1):
                for y in range(j, n+1):
                    res += matrix[x][y]
            return res
        

        # for item in matrix:
        #     item.sort()
        # matrix.sort()

        max_sum = -float('inf')
        row_num, col_num = len(matrix), len(matrix[0])
        for row in range(row_num):
            for col in range(col_num):
                for i in range(row+1):
                    for j in range(col+1):
                        currnet_sum = get_sum(i, j, row, col)
                        if currnet_sum > k:
                            continue
                        max_sum = max(max_sum, currnet_sum)
        # print(f'max_sum = {max_sum}')
        return max_sum

        # i, j = 0, 0
        # while i <= m and j <= n:
        #     current_sum = get_sum(i, j, m, n)
        #     max_sum = max(current_sum, max_sum)



def test(test_name, matrix, k, expected):
    res = Solution().maxSumSubmatrix(matrix, k)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    matrix1 = [
        [1,0,1],
        [0,-2,3]
    ]
    k1 = 2
    expected1 = 2
    test('test1', matrix1, k1, expected1)

    matrix2 = [[2,2,-1]]
    k2 = 3
    expected2 = 3
    test('test2', matrix2, k2, expected2)

    matrix3 = [[2,2,-1]]
    k3 = 0
    expected3 = -1
    test('test3', matrix3, k3, expected3)
