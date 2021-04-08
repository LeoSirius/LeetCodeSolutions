from typing import *

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
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

    nums2 = [4,5,6,7,0,1,2]
    expected2 = 0
    test('test2', nums2, expected2)

    nums3 = [11,13,15,17]
    expected3 = 11
    test('test3', nums3, expected3)
