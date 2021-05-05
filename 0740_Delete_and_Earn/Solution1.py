from typing import *

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        _max = max(nums)
        idx2cnt = [0] * (_max + 1)

        for n in nums:
            idx2cnt[n] += 1

        dp = [0] * (_max+1)   # dp[0] 不用
        dp[1] = idx2cnt[1] * 1
        dp[2] = max(dp[1], idx2cnt[2] * 2)
        for i in range(_max+1):
            dp[i] = max(dp[i-1], dp[i-2] + i * idx2cnt[i])

        return dp[-1]


def test(test_name, nums, expected):
    res = Solution().deleteAndEarn(nums)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    nums1 = [3,4,2]
    expected1 = 6
    test('test1', nums1, expected1)

    nums2 = [2,2,3,3,3,4]
    expected2 = 9
    test('test2', nums2, expected2)

    nums3 = [1]
    expected3 = 1
    test('test3', nums3, expected3)
