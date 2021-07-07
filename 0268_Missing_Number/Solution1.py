from typing import *


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        _sum = (n * (n+1)) // 2
        for n in nums:
            _sum -= n
        return _sum


def test(test_name, nums, expected):
    res = Solution().missingNumber(nums)
    if res == expected:
        print(test_name + ' succeed')
    else:
        print(test_name + ' fail')


if __name__ == '__main__':
    nums1 = [3,0,1]
    expected1 = 2
    test('test1', nums1, expected1)

    nums2 = [0,1]
    expected2 = 2
    test('test2', nums2, expected2)

    nums3 = [9,6,4,2,3,5,7,0,1]
    expected3 = 8
    test('test3', nums3, expected3)

    nums4 = [0]
    expected4 = 1
    test('test4', nums4, expected4)
