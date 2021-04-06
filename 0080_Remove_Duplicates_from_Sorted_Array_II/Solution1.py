from typing import *

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        tail = 2

        for i in range(2, len(nums)):
            if nums[i] > nums[tail-2]:
                nums[tail] = nums[i]
                tail += 1

        return tail


def test(test_name, nums, expected_arr):
    expected_len = Solution().removeDuplicates(nums)
    if expected_len == len(expected_arr) and nums[:expected_len] == expected_arr:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    nums1 = [1,1,1,2,2,3]
    expected_arr1 = [1,1,2,2,3]
    test('test1', nums1, expected_arr1)

    nums2 = [0,0,1,1,1,1,2,3,3]
    expected_arr2 = [0,0,1,1,2,3,3]
    test('test2', nums2, expected_arr2)
