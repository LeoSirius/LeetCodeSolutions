from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            elif target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        return l


def test(test_name, nums, target, expected):
    res = Solution().searchInsert(nums, target)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == '__main__':
    nums1 = [1,3,5,6]
    target1 = 5
    expected1 = 2
    test('test1', nums1, target1, expected1)

    nums2 = [1,3,5,6]
    target2 = 2
    expected2 = 1
    test('test2', nums2, target2, expected2)

    nums3 = [1,3,5,6]
    target3 = 7
    expected3 = 4
    test('test3', nums3, target3, expected3)

    nums4 = [1,3,5,6]
    target4 = 0
    expected4 = 0
    test('test4', nums4, target4, expected4)
