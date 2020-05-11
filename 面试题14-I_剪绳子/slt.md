### 思路1 dp

dp[i] = max(dp[i], max(j * (i-j), j * dp[i-j]))

max 第一个参数 dp[i] 表示不剪，
j * (i-j)   表示 从j处剪一下，剩下i-j不剪了
j * dp[i-j] 表示 从j处剪一下，剩下i-j继续剪
