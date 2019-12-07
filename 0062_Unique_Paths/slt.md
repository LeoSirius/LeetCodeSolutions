### 思路1 dp

注意用dfs会超时。

Since the robot can only move right and down, when it arrives at a point, it either arrives from left or above. If we use dp[i][j] for the number of unique paths to arrive at the point (i, j), then the state equation is dp[i][j] = dp[i][j - 1] + dp[i - 1][j]. Moreover, we have the base cases dp[0][j] = dp[i][0] = 1 for all valid i and j.


### 思路2 组合公式

一个m行，n列的矩阵，机器人从左上走到右下总共需要的步数是m+n-2，其中向下走的步数是m-1，因此问题变成了在m+n-2个操作中，选择m–1个时间点向下走`C（（m+n-2），（m-1））`
