### Solution1 dp

_max = max(nums)

然后对 [1, _max] 进行 dp

- 对当前数字 n，如果不删除，则就是 n - 1 的最优结果
- 对当前数组 n，如果删除，则就是 n - 2 的最优结果 + (当前数组的个数 * 当前数字)

用一个数组 idx2cnt 存放每个数字出现的个数

dp[i] = max(dp[i-1], dp[i-2] + i * idx2cnt)
