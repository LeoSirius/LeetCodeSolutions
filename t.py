from typing import *

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        if not nums:
            return res

        l, r = 0, len(nums)-1

        while l < r:
            m = l + (r - l) // 2
            if target < nums[m]:
                r = m - 1
            elif target == nums[m]:
                r = m
            else:
                l = m + 1
        if nums[l] == target:
            res[0] = l

        r = len(nums) - 1
        while l < r:
            m = l + (r - l) // 2 + 1
            if target < nums[m]:
                r = m - 1
            elif target == nums[m]:
                l = m
            else:
                l = m + 1
        if nums[r] == target:
            res[1] = r
        return res


def test(test_name, nums, target, expected):
    res = Solution().searchRange(nums, target)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    nums1 = [5,7,7,8,8,10]
    target1 = 8
    expected1 = [3,4]
    test('test1', nums1, target1, expected1)

    nums2 = [5,7,7,8,8,10]
    target2 = 6
    expected2 = [-1, -1]
    test('test2', nums2, target2, expected2)

    nums3 = []
    target3 = 0
    expected3 = [-1, -1]
    test('test3', nums3, target3, expected3)
