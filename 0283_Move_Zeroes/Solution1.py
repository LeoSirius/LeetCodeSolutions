from typing import *

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                p = i
                while p < len(nums) - 1 and nums[p] == 0:
                    p += 1
                nums[i], nums[p] = nums[p], nums[i]


def test(test_name, nums, expected):
    Solution().moveZeroes(nums)
    if nums == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    nums1 = [0,1,0,3,12]
    expected1 = [1,3,12,0,0]
    test('test1', nums1, expected1)

    nums2 = [1,0]
    expected2 = [1,0]
    test('test2', nums2, expected2)


# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

# 示例:

# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
# 说明:

# 必须在原数组上操作，不能拷贝额外的数组。
# 尽量减少操作次数。
