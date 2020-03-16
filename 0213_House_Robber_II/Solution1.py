from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]

        dp1 = [0 for i in range(len(nums))]
        dp2 = [0 for i in range(len(nums))]
        dp1[0] = dp1[1] = nums[0]
        dp2[1] = nums[1]

        for i in range(2, len(nums)):
            dp1[i] = max(dp1[i-2] + nums[i], dp1[i-1])
            dp2[i] = max(dp2[i-2] + nums[i], dp2[i-1])

        return max(dp1[-2], dp2[-1])

def test(test_name, nums, expected):
    res = Solution().rob(nums)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == "__main__":
    nums1 = [2,3,2]
    expected1 = 3
    test('test1', nums1, expected1)

    nums2 = [1,2,3,1]
    expected2 = 4
    test('test2', nums2, expected2)
