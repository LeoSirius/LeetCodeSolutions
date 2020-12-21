### 思路1

dp[i][j]表示 从前往后拼，key的第i个字符，ring的第j个字符往12点对齐最少的步数

显然，ring的第j个字符和key的第i个字符必须相等才行，

对key的第i个字符，假设是x，需要考虑x在ring中下标的集合。

因此对每一次字符，维护一个数组pos[i]，表示x在ring中的位置的集合


对与dp[i][j]，需要枚举上次的字符pos[i-1]，在ring中的所有位置k。

for k in pos[i-1]
    min {
        dp[i-1][k] + min( abs(j-k), n - abs(j-k) ) + 1
    }

min中的三部分：

- dp[i-1][k]：上次的值
- min( abs(j-k), n - abs(j-k) )，k转到上次j的位置的步数。因为是环，所以有后面的`n - abs(j-k)`
- 1：按下


空间复杂度O(mn)
时间复杂度O(mn^2)

m是key的长度，n是ring的长度。由于用了pos，所以O(mn^2)是一个宽泛的上界。