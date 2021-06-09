### Solution1 DP

参考

- 时间复杂度 O(len * n * minProfit) len 为 group 长度
- 空间复杂度 O(len * n * minProfit)

`dp[i][j][k]` 表示在前 i 个工作中选择了 j 个员工，并且满足工作利润至少为 k 的计划数目。

设 group 数组长度为 n，则最后的结果为

sum(dp[len][j][minProfit] for j in range(n))

对于每个工作 i，在员工为 j 的情况下，有「当前可以开展工作」和「当前无法开展工作」两种情况。

如果当前工作 i 无法开展，则

dp[i][j][k] = dp[i-1][j][k]

如果当前工作 i 可以开展，则（`j-group[i]`是）

dp[i][j][k] = dp[i-1][j][k] + dp[i-1][j-group[i]][max(0, k-profit[i])]