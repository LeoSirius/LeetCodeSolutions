### 思路1 

泛化到k次交易，秒杀所有股票交易问题

dp[k, i] = max(dp[k, i-1], prices[i] - prices[j] + dp[k-1, j-1]),     j=[0..i-1]

dp[k, i] 表示k次交易，第i天卖（或不交易）时的最大收益

两种情况：

- i天不交易，则dp[k,i] = dp[k, i-1]
- i天交易(卖)，假设我们在j天买了，则dp[k,i] = prices[i] - prices[j] + dp[k-1, j-1]



j是可以等于i的，j=i，则
dp[k,i] = max(dp[k,i-1], dp[k-1][i-1])

