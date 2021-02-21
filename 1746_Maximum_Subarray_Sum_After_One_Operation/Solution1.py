from typing import *


class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        res = -float('inf')
        replace, nonreplace = 0, 0

        for n in nums:
            replace = max(n * n, n + replace, n * n + nonreplace)
            nonreplace = max(n, n + nonreplace)
            res = max(res, replace, nonreplace)

        return res


def test(test_name, nums, expected):
    res = Solution().maxSumAfterOperation(nums)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    nums1 = [2,-1,-4,-3]
    expected1 = 17
    test('test1', nums1, expected1)

    nums2 = [1,-1,1,1,-1,-1,1]
    expected2 = 4
    test('test2', nums2, expected2)

