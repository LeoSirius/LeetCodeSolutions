from typing import *

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, n in enumerate(nums):
            l, r = i + 1, len(nums) - 1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while l < r:
                _sum = nums[l] + nums[r] + n
                if _sum == 0:
                    res.append([nums[l], nums[r], n])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]: l += 1
                    while l < r and nums[r] == nums[r+1]: r -= 1
                elif _sum > 0:
                    r -= 1
                else:
                    l += 1

        return res


def test(test_name, nums, expected):
    res = Solution().threeSum(nums)
    [item.sort() for item in res]
    res.sort()
    [item.sort() for item in expected]
    expected.sort()
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    nums1 = [-1, 0, 1, 2, -1, -4]
    expected1 = [
        [-1, 0, 1],
        [-1, -1, 2]
    ]
    test('test1', nums1, expected1)

    nums2 = [0,0]
    expected2 = []
    test('test2', nums2, expected2)
