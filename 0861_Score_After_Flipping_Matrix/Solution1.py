from typing import *

class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        res = 0

        for j in range(n):
            one_cnt = 0
            for i in range(m):
                if A[i][0] == 1:
                    one_cnt += A[i][j]
                else:
                    one_cnt += (1-A[i][j])
            k = max(one_cnt, m-one_cnt)
            res += k * (1 << (n-j-1))
        return res


def test(test_name, A, expected):
    res = Solution().matrixScore(A)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    A1 = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
    expected1 = 39
    test('test1', A1, expected1)


# 有一个二维矩阵 A 其中每个元素的值为 0 或 1 。
# 移动是指选择任一行或列，并转换该行或列中的每一个值：将所有 0 都更改为 1，将所有 1 都更改为 0。
# 在做出任意次数的移动后，将该矩阵的每一行都按照二进制数来解释，矩阵的得分就是这些数字的总和。
# 返回尽可能高的分数。

# 示例：

# 输入：[[0,0,1,1],[1,0,1,0],[1,1,0,0]]
# 输出：39
# 解释：
# 转换为 [[1,1,1,1],[1,0,0,1],[1,1,1,1]]
# 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
#  

# 提示：

# 1 <= A.length <= 20
# 1 <= A[0].length <= 20
# A[i][j] 是 0 或 1

