### 思路1 dp

二维dp，代表第n个房子刷第1、2、3种颜色时，最小的花费。最后只需要返回三种颜色中的最小值即可。递推关系为

当前房子刷0，则i-1房子必须刷1或2。其他同理

dp[i][0] = Math.min(dp[i-1][1],dp[i-1][2])+costs[i][0];
dp[i][1] = Math.min(dp[i-1][0],dp[i-1][2])+costs[i][1];
dp[i][2] = Math.min(dp[i-1][1],dp[i-1][0])+costs[i][2];
