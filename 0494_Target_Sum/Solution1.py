from typing import *

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        def dfs(idx, presum):
            if (idx, presum) in cache:
                return cache[(idx, presum)]
            res = 0
            if idx >= len(nums):
                return res
            if idx == len(nums)-1:
                if presum + nums[idx] == target:
                    res += 1
                if presum - nums[idx] == target:
                    res += 1
                cache[(idx, presum)] = res
                return res
            for n  in [nums[idx], -nums[idx]]:
                res += dfs(idx+1, presum + n)
            cache[(idx, presum)] = res
            return res

        return dfs(0, 0)


def test(test_name, nums, target, expected):
    res = Solution().findTargetSumWays(nums, target)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    nums1 = [1,1,1,1,1]
    target1 = 3
    expected1 = 5
    test('test1', nums1, target1, expected1)

    nums2 = [1]
    target2 = 1
    expected2 = 1
    test('test2', nums2, target2, expected2)

    nums3 = [1, 0]
    target3 = 1
    expected3 = 2
    test('test3', nums3, target3, expected3)
