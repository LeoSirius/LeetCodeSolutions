### 思路1 dp

- 时间复杂度 O(n * sqrt(n))
- 空间复杂度 O(n)

For each i, it must be the sum of some number `(i - j*j)` and a perfect square number (j*j). 即 i = (i - j * j) + (j * j)

dp[n]表示最少使用的个数，则有(k为满足k^2<=n的最大的k)

转移方程

dp[i] = min(dp[i], dp[i-j*j])