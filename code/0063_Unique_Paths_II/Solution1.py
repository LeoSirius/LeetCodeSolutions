from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        dp[1][0] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                if obstacleGrid[i-1][j-1] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m][n]


def test(test_name, obstacleGrid, expected):
    res = Solution().uniquePathsWithObstacles(obstacleGrid)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    obstacleGrid1 = [
        [0,0,0],
        [0,1,0],
        [0,0,0]
    ]
    expected1 = 2
    test('test1', obstacleGrid1, expected1)

    obstacleGrid2 = [[0,0]]
    expected2 = 1
    test('test2', obstacleGrid2, expected2)
