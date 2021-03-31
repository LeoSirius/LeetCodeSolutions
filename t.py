from typing import *

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i, n in enumerate(nums):
            num2find = target - n
            if num2find in mp:
                return [i, mp[num2find]]
            mp[n] = i
        return []


def test(test_name, nums: List[int], target: int, expected: List[int]):
    slt = Solution()
    res = slt.twoSum(nums, target)
    if sorted(res) == sorted(expected):
        print(test_name + ' success')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    nums1 = [2, 7, 11, 15]
    target1 = 9
    expected1 = [0,1]
    test('test1', nums1, target1, expected1)
