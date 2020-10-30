from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for idx, num in enumerate(nums):
            num_to_find = target - num
            if num_to_find in d.keys():
                return [idx, d[num_to_find]]
            d[num] = idx

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
