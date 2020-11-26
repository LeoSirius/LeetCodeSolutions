### 思路1 桶

- 把所有数按一定区间大小放到桶中
- max(当前桶中的最小值 - 前一个桶中的最大值)就是最后的结果

时间复杂度O(N)
for len(桶s)：
  min(current 桶)

len(桶s) * len(current 桶) = N

空间复杂度O(N)

关键是如何确定每个桶的长度，可以参考

https://leetcode-cn.com/problems/maximum-gap/solution/python3-tong-pai-xu-by-yanghk/

https://leetcode-cn.com/problems/maximum-gap/solution/zui-da-jian-ju-by-leetcode-solution/

