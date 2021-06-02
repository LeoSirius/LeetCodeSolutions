### Solution1 前缀和 + hash + 同余

- 时间复杂度 O(n)
- 空间复杂度 O(n)

直接暴力双重循环的话会超时

假设我们的目标区间是 `[i, j]`

有 

`presum[j] - presum[i-1] = n * k` 其中 n 为整数

变形

`(presum[j] / k) - (presum[i-1] / k) = n`

要使两者除 k 相减为整数，则需要 presum[j] 和 presum[i-1] 对 k 的余数相同

解释：

假设:
sum[i] = k * a + b
sum[j] = k * c + d
那么：sum[i] - sum[j] = (k * a + b) - (k * c + d) = k * (a - c) + (b - d)
要使 (sum[i] - sum[j]) 是 k 的整数倍，就要使 b - d = 0, 即 sum[i] 与 sum[j] 除 k 余数相同
