from typing import *


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            n2find = target - n
            if n2find in d:
                return [i, d[n2find]]
            d[n] = i
        return []


def test(test_name, nums: List[int], target: int, expected: List[int]):
    res = Solution().twoSum(nums, target)
    res.sort()
    expected.sort()
    if res == expected:
        print(test_name + ' success')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    nums1 = [2, 7, 11, 15]
    target1 = 9
    expected1 = [0,1]
    test('test1', nums1, target1, expected1)
