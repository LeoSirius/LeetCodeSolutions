### Solution1 DP


参考 https://leetcode-cn.com/problems/last-stone-weight-ii/solution/java-gao-kao-bei-bei-bao-zhi-jing-gao-zh-ybd8/


设总重量为 sum，要减去的石头总重量为 neg
则加法运算求得的石头总重量为 sum - neg
最后结果的重量为 sum - neg - neg = sum - 2 * neg
要最后的结果最小，即要求 neg 最接近 sum / 2


dp[i] 表示：是否有子集数组，重量和为i，值为 True or False

