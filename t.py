from typing import *

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                _sum = nums[i] + nums[l] + nums[r]
                if _sum > target:
                    r -= 1
                elif _sum < target:
                    l += 1
                else:
                    return target
                if abs(target - _sum) < abs(target - res):
                    res = _sum

        return res


def test(test_name, nums, target, expected):
    slt = Solution()
    res = slt.threeSumClosest(nums, target)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    nums1 = [-1, 2, 1, -4]
    target1 = 1
    expected1 = 2
    test('test1', nums1, target1, expected1)

    nums2 = [0,2,1,-3]
    target2 = 1
    expected2 = 0
    test('test2', nums2, target2, expected2)