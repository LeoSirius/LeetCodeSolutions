from typing import *

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p, tail = 0, 0
        while p < len(nums):
            if nums[tail] != nums[p]:
                nums[tail+1] = nums[p]
                tail += 1
            p += 1
        return tail + 1


def test(test_name, nums, expected):
    res = Solution().removeDuplicates(nums)
    if nums[:res] == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    nums1 = [1, 1, 2]
    expected1 = [1,2]
    test('test1', nums1, expected1)

    nums2 = []
    expected2 = []
    test('test2', nums2, expected2)

    nums3 = [1, 1]
    expected3 = [1]
    test('test3', nums3, expected3)

    nums4 = [0,0,1,1,1,2,2,3,3,4]
    expected4 = [0,1,2,3,4]
    test('test4', nums4, expected4)