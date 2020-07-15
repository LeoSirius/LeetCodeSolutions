from typing import *

class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [0 for _ in range(n)]
        for row in range(m):
            dp[0] += grid[row][0]   # 每行的第一个元素单独处理
            for col in range(1,n):
                dp[col] = max(dp[col-1], dp[col]) + grid[row][col]
        return dp[-1]


def test(test_name, grid, expected):
    res = Solution().maxValue(grid)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == "__main__":
    grid1 = [
        [1,3,1],
        [1,5,1],
        [4,2,1]
    ]
    expected1 = 12
    test('test1', grid1, expected1)

    grid2 = [
        [1,2],
        [5,6],
        [1,1]
    ]
    expected2 = 13
    test('test2', grid2, expected2)


# 在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。
# 你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。
# 给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

# 示例 1:
# 输入: 
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# 输出: 12

# 解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物
#  
# 提示：
# 0 < grid.length <= 200
# 0 < grid[0].length <= 200
