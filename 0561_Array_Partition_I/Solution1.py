from typing import *


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = 0

        for i in range(0, len(nums), 2):
            res += nums[i]

        return res


def test(test_name, nums, expected):
    res = Solution().arrayPairSum(nums)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    nums1 = [1,4,3,2]
    expected1 = 4
    test('test1', nums1, expected1)

    nums2 = [6,2,6,5,1,2]
    expected2 = 9
    test('test2', nums2, expected2)

