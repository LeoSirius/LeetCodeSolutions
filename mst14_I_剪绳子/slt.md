### 思路1 dp

for i = 2; i <= n; i++
  for j = 1; j < i; j++
    dp[i] = max(dp[i], max(j * (i-j), j * dp[i-j]))

i表示剪成多少段。如n=5，则最少是2段，最多是5段。（mn都是整数）

j遍历i剪完的每一段。比如i=2，则j=1，2.表示在第一段和第二段中再剪下去。

max 第一个参数 dp[i] 表示不剪，
j * (i-j)   表示 从j处剪一下，剩下i-j不剪了
j * dp[i-j] 表示 从j处剪一下，剩下i-j继续剪

### 思路2 贪心

贪心算法，取3，具体见。

https://leetcode-cn.com/problems/jian-sheng-zi-ii-lcof/solution/mian-shi-ti-14-ii-jian-sheng-zi-iitan-xin-er-fen-f/

贪心法则：尽可能分解出多的 3, 3的个数为a，余数为b，b可能的值是0,1,2

b = 0, return 3^a
b = 1, 将末尾的3+1看成4，返回3^(a-1) + 2 * 2
b = 2, 返回3^a * 2