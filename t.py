from typing import *

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:

        res = -float('inf')
        row_num, col_num = len(matrix), len(matrix[0])
        # print(f'col_num = {col_num}')
        dp = [[0] * (col_num+1) for _ in range(row_num+1)]
        dp = [dp for _ in range(col_num+1)]
        dp = [dp for _ in range(row_num+1)]
        print(f'lendp = {len(dp)}, lendp0 = {len(dp[0])}, lendp00 = {len(dp[0][0])}, lendp000 = {len(dp[0][0][0])}')

        for i1 in range(1, row_num+1):
            for j1 in range(1, col_num+1):
                dp[i1][j1][i1][j1] = matrix[i1][j1]
                if dp[i1][j1][i1][j1] <= k:
                    res = max(res, dp[i1][j1][i1][j1])
                for i2 in range(i1, row_num+1):
                    for j2 in range(j1, col_num+1):
                        dp[i1][j1][i2][j2] = dp[i1][j1][i2-1][j2] + dp[i1][j1][i2][j2 - 1] - dp[i1][j1][i2-1][j2 -1] + matrix[i2][j2]
                        print(f'{i1} {j1} {i2} {j2} dp = {dp[i1][j1][i2][j2]}')
                        if dp[i1][j1][i2][j2] <= k:
                            res = max(res, dp[i1][j1][i2][j2])
        print(f'res = {res}')
        return res



        # for row in range(row_num):
        #     for col in range(col_num):
        #         for i in range(row+1):
        #             for j in range(col+1):
        #                 currnet_sum = get_sum(i, j, row, col)
        #                 if currnet_sum > k:
        #                     continue
        #                 max_sum = max(max_sum, currnet_sum)
        # return max_sum


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
    # test('test1', matrix1, k1, expected1)

    # matrix2 = [[2,2,-1]]
    # k2 = 3
    # expected2 = 3
    # test('test2', matrix2, k2, expected2)

    # matrix3 = [[2,2,-1]]
    # k3 = 0
    # expected3 = -1
    # test('test3', matrix3, k3, expected3)

    matrix4 = [
        [5,-4,-3,4],
        [-3,-4,4,5],
        [5,1,5,-4]]
    k4 = 10
    expected4 = 10
    test('test4', matrix4, k4, expected4)
