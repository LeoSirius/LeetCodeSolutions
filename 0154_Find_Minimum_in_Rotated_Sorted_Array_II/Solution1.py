from typing import *


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                r = m
            elif nums[m] > nums[r]:
                l = m + 1
            else:
                r -= 1
        return nums[l]


def test(test_name, nums, expected):
    res = Solution().findMin(nums)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == '__main__':
    nums1 = [3,4,5,1,2]
    expected1 = 1
    test('test1', nums1, expected1)

    nums2 = [2,2,2,0,1]
    expected2 = 0
    test('test2', nums2, expected2)

    nums3 = [1,3,3]
    expected3 = 1
    test('test3', nums3, expected3)

    nums4 = [3,3,1,3]
    expected4 = 1
    test('test4', nums4, expected4)

