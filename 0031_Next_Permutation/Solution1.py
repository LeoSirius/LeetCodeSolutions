from typing import *


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # idx_max: 最大元素的idx
        # idx_big: 從右向左 比 idx_max - 1 元素大的 idx

        # 兩種特殊情況
        # case1：降序，312，在第一個循環裡i == 0時返回
        # case2：正序，123，這時 idx_max 和 idx_big 都等於最後一個元素。swap 最後兩個元素，然後結束
        for i in range(len(nums) - 1, -1, -1):
            if i == 0:
                nums.reverse()
                return
            if nums[i-1] < nums[i]:
                idx_max = i
                break

        idx_big = len(nums) - 1
        for i in range(len(nums) - 1, idx_max - 1, -1):
            if nums[i] > nums[idx_max-1]:
                idx_big = i
                break

        nums[idx_big], nums[idx_max-1] = nums[idx_max-1], nums[idx_big]

        i, j = idx_max, len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1


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
