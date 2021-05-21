### Solution1 dp

- 时间复杂度 O(m * n)
- 空间复杂度 O(m * n)

dp[i][j] 表示 nums1 中前 i 个数字和 nums2 中前 j 个数组可以组成最多直线数量

转移方程：

- dp[i][j] = dp[i-1][j-1] + 1,            if nums[i] == nums[j]
- dp[i][j] = max(dp[i-1][j], dp[i][j-1]), if nums[i] != nums[j]

若 nums[i] != nums[j]，说明他们中至少一个不能对结果做出贡献，取其中最大值
