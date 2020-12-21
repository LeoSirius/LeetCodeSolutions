from typing import *

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def is_mid_after_k(mid):
            i, j = 0, n-1
            cnt = 0
            while i < n and 0 <= j:
                if matrix[i][j] <= mid:
                    i += 1
                    cnt += j + 1
                else:
                    j -= 1
            return k <= cnt

        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = left + (right - left) // 2
            if is_mid_after_k(mid):
                right = mid
            else:
                left = mid + 1
        return left


def test(test_name, matrix, k, expected):
    res = Solution().kthSmallest(matrix, k)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == "__main__":
    matrix1 = [
        [ 1,  5,  9],
        [10, 11, 13],
        [12, 13, 15]
    ]
    k1 = 8
    expected1 = 13
    test('test1', matrix1, k1, expected1)

    matrix2 = [
        [1,2],
        [1,3]
    ]
    k2 = 2
    expected2 = 1
    test('test2', matrix2, k2, expected2)

# Given a n x n matrix where each of the rows and columns are sorted in
#  ascending order, find the kth smallest element in the matrix.

# Note that it is the kth smallest element in the sorted order, 
# not the kth distinct element.

# Example:

# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,

# return 13.
# Note:
# You may assume k is always valid, 1 ≤ k ≤ n2.
