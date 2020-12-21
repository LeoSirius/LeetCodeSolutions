from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]

        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[-1]


def test(test_name, nums, expected):
    res = Solution().rob(nums)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == "__main__":
    nums1 = [1,2,3,1]
    expected1 = 4
    test('test1', nums1, expected1)

    nums2 = [2,7,9,3,1]
    expected2 = 12
    test('test2', nums2, expected2)

    nums3 = []
    expected3 = 0
    test('test3', nums3, expected3)

    nums4 = [2,1,1,2]
    expected4 = 4
    test('test4', nums4, expected4)
