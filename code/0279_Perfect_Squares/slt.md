### 思路1 dp

For each i, it must be the sum of some number `(i - j*j)` and a perfect square number (j*j). 即 i = (i - j * j) + (j * j)

dp[n]表示最少使用的个数，则有(k为满足k^2<=n的最大的k)

dp[n] = 1 + min(dp[n-1^2],dp[n-2^2],dp[n-3^2], ...dp[n-k^2])
意思是：n时，最少使用的个数 = min(dp[n-1^2],dp[n-2^2],dp[n-3^2], ...dp[n-k^2]) 在加上一个 j * j


定义一个函数f(n)表示我们要求的解。f(n)的求解过程为：
f(n) = 1 + min{
  f(n-1^2), f(n-2^2), f(n-3^2), f(n-4^2), ... , f(n-k^2) //
}
