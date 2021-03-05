from typing import *

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            l, r = i, len(nums) - 1
            while l < r:
                kkkk


def test(test_name, nums, expected):
    res = Solution().threeSum(nums)
    res = [item.sort() for item in res]
    expected = [item.sort() for item in expected]
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
