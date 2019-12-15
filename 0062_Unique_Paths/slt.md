### 思路1 dp

注意用dfs会超时。

Since the robot can only move right and down, when it arrives at a point, it either arrives from left or above. If we use dp[i][j] for the number of unique paths to arrive at the point (i, j), then the state equation is dp[i][j] = dp[i][j - 1] + dp[i - 1][j]. Moreover, we have the base cases dp[0][j] = dp[i][0] = 1 for all valid i and j.

`res[i][j] = res[i-1][j] + res[i][j-1];`

优化一下可以写成

`cur[j] = pre[j] + cur[j-1];`

实际上pre[j]就是cur[j]更新之前，最后还可以优化成

`dp[j] += dp[j-1];`

这样空间复杂度只有O(n)

### 思路2 组合公式

一个m行，n列的矩阵，机器人从左上走到右下总共需要的步数是m+n-2，其中向下走的步数是m-1，因此问题变成了在m+n-2个操作中，选择m–1个时间点向下走`C（（m+n-2），（m-1））`

在算组合的时候也不用去求阶乘。

Combination(N, k) = n! / (k!(n - k)!)
reduce the numerator and denominator and get
C = ( (n - k + 1) * (n - k + 2) * ... * n ) / k!
