### 思路1 dp

dp[i]表示字符串s的前i个字符能否拆分成wordDict。
注意dp中i和j是从1开始，而s中是索引
dp[i] = dp[j] && s.substr(j, i-j) in wordDic
