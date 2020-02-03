### 思路1 dp

dp[i]表示到i为止，能打劫的最大数。

dp[i] = max(dp[i-2] + nums[i], dp[i-1]);
