### 思路1 dp

当前nums[i]就两种情况，要么加入之前的数，要么自己门派开启一个新的subarray

所有已状态转移方程

dp[i] = max(dp[i-1] + nums[i], nums[i])

dp[i]就表示已i这个数结尾的最大subarray的最大sum。

最后要返回的是max(dp[i])
