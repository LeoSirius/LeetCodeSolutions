### 思路1 dp 逆向思维


这道题的意思是，最坏情况下，最少扔几次

https://leetcode.com/problems/super-egg-drop/discuss/158974/C%2B%2BJavaPython-2D-and-1D-DP-O(KlogN)

用逆向思维

dp[m][k]表示k个鸡蛋，m次操作，所能确定的楼层数量n

我们需要让能确定的楼层数量n > N，表示我们用k个鸡蛋扔了m次能覆盖题目给的N层楼

- 蛋碎了，k-1，m-1，说明在操作的这一层下面，
- 蛋没碎，k, m-1，说明真正的N在操作的这一层上面

（当前楼层下面，能覆盖的楼层数量 + 当前楼层上面，能覆盖的楼层数量 + 当前楼层1）就是k个鸡蛋，f次扔，能确定的楼层的总数量

dp[m][k] = dp[m-1][k-1] + dp[m-1][k] + 1

- 当前层蛋碎了，则能确定dp[m-1][k-1]个楼层数
- 当前层蛋没碎，则能确定dp[m-1][k]个楼层数
- 再加上当前层自己1层


## 思路2 dp + 二分查找

见 https://leetcode-cn.com/problems/super-egg-drop/solution/ji-dan-diao-luo-by-leetcode-solution-2/
