from typing import *

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        pivot = N - 1
        for i in range(N - 1, -1, -1):
            if i == 0:
                nums.reverse()
                return
            if nums[i] > nums[i-1]:
                pivot = i
                break
        
        idx = N
        for i in range(N - 1, pivot - 1, -1):
            if nums[i] > nums[pivot - 1]:
                idx = i
                break
        
        nums[pivot-1], nums[i] = nums[i], nums[pivot-1]
        l, r = pivot, N - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1


def test(test_name, nums, expected):
    Solution().nextPermutation(nums)
    if nums == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    nums1 = [1,2,3]
    expected1 = [1,3,2]
    test("test1", nums1, expected1)

    nums2 = [3,2,1]
    expected2 = [1,2,3]
    test("test2", nums2, expected2)

    nums3 = [1,1,5]
    expected3 = [1,5,1]
    test("test3", nums3, expected3)

    nums4 = [1,3,2]
    expected4 = [2,1,3]
    test("test4", nums4, expected4)


