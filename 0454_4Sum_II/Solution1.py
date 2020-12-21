from typing import *
from collections import defaultdict

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        sum_ab = defaultdict(int)
        res = 0
        for a in A:
            for b in B:
                sum_ab[a+b] += 1

        for c in C:
            for d in D:
                target = -(c+d)
                if sum_ab[target] > 0:
                    res += sum_ab[target]
        return res


def test(test_name, A, B, C, D, expected):
    res = Solution().fourSumCount(A, B, C, D)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    A1 = [1,2]
    B1 = [-2,-1]
    C1 = [-1,2]
    D1 = [0, 2]
    expected1 = 2
    test('test1', A1, B1, C1, D1, expected1)

    A2 = [-1,-1]
    B2 = [-1,1]
    C2 = [-1,1]
    D2 = [1,-1]
    expected2 = 6
    test('test2', A2, B2, C2, D2, expected2)



# 给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，
# 使得 A[i] + B[j] + C[k] + D[l] = 0。

# 为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。
# 所有整数的范围在 -228 到 228 - 1 之间，最终结果不会超过 231 - 1 。

# 例如:

# 输入:
# A = [ 1, 2]
# B = [-2,-1]
# C = [-1, 2]
# D = [ 0, 2]

# 输出:
# 2

# 解释:
# 两个元组如下:
# 1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0

