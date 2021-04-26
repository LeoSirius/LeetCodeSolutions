from typing import *

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:

        res = float('-inf')
        row_num, col_num = len(matrix), len(matrix[0])
        
        for l in range(col_num):
            _sum = [0] * row_num   # 以 l 为边界，每行的和
            for r in range(l, col_num):
                pre_sum_matrix = [0] * row_num
                for j in range(row_num):
                    _sum[j] += matrix[j][r]
                    pre_sum_matrix[j] = _sum[j]
                    print(f'pre = {l, r, j} {pre_sum_matrix}')
                #     if pre_sum_matrix <= k:
                #         res = max(res, pre_sum_matrix)
                #     if _sum[j] <= k:
                #         res = max(res, _sum[j])
                # print(f'_sum[j]')

                # for item in pre_sum_matrix:
                #     if item <= k:
                #         res = max(res, item)
        return res


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

    # matrix4 = [
    #     [5,-4,-3,4],
    #     [-3,-4,4,5],
    #     [5,1,5,-4]]
    # k4 = 10
    # expected4 = 10
    # test('test4', matrix4, k4, expected4)

    # matrix5 = [
    #     [5,-4,-3,4],
    #     [-3,-4,4,5],
    #     [5,1,5,-4]]
    # k5 = 9
    # expected5 = 9
    # test('test5', matrix5, k5, expected5)

    matrix6 = [
        [5,-4,-3,4],
        [-3,-4,4,5],
        [5,1,5,-4]]
    k6 = 8
    expected6 = 8
    test('test6', matrix6, k6, expected6)
