from typing import *

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = [0] * 32
        for n in nums:
            for j in range(32):
                counts[j] += n & 1
                n >>= 1

        res, m = 0, 3
        for i in range(32):
            res <<= 1
            res |= counts[31-i] % m

        return res if counts[31] % m == 0 else ~(res ^ 0xffffffff)


def test(test_name, nums, expected):
    res = Solution().singleNumber(nums)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    nums1 = [2,2,3,2]
    expected1 = 3
    test('test1', nums1, expected1)

    nums2 = [0,1,0,1,0,1,99]
    expected2 = 99
    test('test2', nums2, expected2)

    nums3 = [-2,-2,1,1,4,1,4,4,-4,-2]
    expected3 = -4
    test('test3', nums3, expected3)
