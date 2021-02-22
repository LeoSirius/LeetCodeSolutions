from typing import *
from functools import lru_cache


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)

        @lru_cache(2000)        # No cache will reach timeout
        def dp(l, i):
            if i == m:
                return 0

            pick_left = dp(l+1, i+1) + nums[l] * multipliers[i]
            pick_right = dp(l, i+1) + nums[n-(i-l)-1] * multipliers[i]

            return max(pick_left, pick_right)

        return dp(0, 0)


def test(test_name, nums, multipliers, expected):
    res = Solution().maximumScore(nums, multipliers)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    nums1 = [1,2,3]
    multipliers1 = [3,2,1]
    expected1 = 14
    test('test1', nums1, multipliers1, expected1)

    nums2 = [-5,-3,-3,-2,7,1]
    multipliers2 = [-10,-5,3,4,6]
    expected2 = 102
    test('test2', nums2, multipliers2, expected2)

