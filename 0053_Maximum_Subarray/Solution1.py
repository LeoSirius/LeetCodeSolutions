from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        dp = [nums[0]]
        for i in range(1, len(nums)):
            dp.append(max(dp[i-1], 0) + nums[i])
            res = max(res, dp[i])
        return res

def test(test_name, nums, expected):
    res = Solution().maxSubArray(nums)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    nums1 = [-2,1,-3,4,-1,2,1,-5,4]
    expected1 = 6
    test('test1', nums1, expected1)

    nums2 = [1]
    expected2 = 1
    test('test2', nums2, expected2)
