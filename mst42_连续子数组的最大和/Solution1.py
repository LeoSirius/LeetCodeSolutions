from typing import *


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(0, dp[i-1]) + nums[i]
        return max(dp)


def test(test_name, nums, expected):
    res = Solution().maxSubArray(nums)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(f'{test_name} failed.')


if __name__ == "__main__":
    nums1 = [-2,1,-3,4,-1,2,1,-5,4]
    expected1 = 6
    test('test1', nums1, expected1)

    nums2 = [-2, -1]
    expected2 = -1
    test('test2', nums2, expected2)


# 输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

# 要求时间复杂度为O(n)。

# 示例1:

# 输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
#  

# 提示：

# 1 <= arr.length <= 10^5
# -100 <= arr[i] <= 100
