from typing import *


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for i, n in enumerate(nums):
            res ^= i
            res ^= n
        res ^= len(nums)
        return res


def test(test_name, nums, expected):
    res = Solution().missingNumber(nums)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    nums1 = [3,0,1]
    expected1 = 2
    test('test1', nums1, expected1)

    nums2 = [9,6,4,2,3,5,7,0,1]
    expected2 = 8
    test('test2', nums2, expected2)

