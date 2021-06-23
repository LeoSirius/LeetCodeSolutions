from typing import *


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - min(nums) * len(nums)


def test(test_name, nums, expected):
    res = Solution().minMoves(nums)
    if type(res) == type(expected) and res == expected:
        print(test_name + ' succeed')
    else:
        print(test_name + ' fail')


if __name__ == '__main__':
    nums1 = [1,2,3]
    expected1 = 3
    test('test1', nums1, expected1)

    nums2 = [1,1,1]
    expected2 = 0
    test('test2', nums2, expected2)
