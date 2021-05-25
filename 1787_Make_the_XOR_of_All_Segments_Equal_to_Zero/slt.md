### Solution1 DP

- 时间复杂度
- 空间复杂度

参考：https://leetcode-cn.com/problems/make-the-xor-of-all-segments-equal-to-zero/solution/gong-shui-san-xie-chou-xiang-cheng-er-we-ww79/

最后的结果要求「答案数组中所有长度为 k 的区间异或结果为 0」

往前倒推

1. `nums[i] ^ nums[i+1] ^ ... ^ nums[j-1] ^ nums[j] = 0`
2. i 前后移动，整体区间异或结果也为 0，有 `nums[i+1] ^ nums[i+2] ^ ... ^ nums[j] ^ nums[j+1] = 0`
3. 两式结合，中间部分异或抵消，有 `nums[i] ^ nums[j+1] = 0` 即 nums[i] == nums[j+1]

所以变换后的数组必然是 k 个数一组不断重复

我们把数组转为 k 列的二维数组，题目变成：

求变换后的二维数组，要求

- 每列相等
- 首行异或值为 0

定义`DP[i][xor]` 表示考虑前 i 列相同，且首行前 i 列异或值为 xor 的最小修改次数

最后要求得结果是`DP[k-1][0]`

第一维的范围：[0, k-1]
第二维的范围：[0, 2^10] （异或为不进位加法，由题目，nums 元素最大 2 ^ 10）





