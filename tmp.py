from typing import *

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1
        i = 0
        while i < len(nums):
            if nums[i] == 0 and l < i:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
            elif nums[i] == 2 and i < r:
                nums[r], nums[i] = nums[i], nums[r]
                r -= 1
            else:
                i += 1
        return nums


def test(test_name, nums, expectd):
    Solution().sortColors(nums)
    print(nums)
    if nums == expectd:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    nums1 = [2,0,2,1,1,0]
    expected1 = [0,0,1,1,2,2]
    test('test1', nums1, expected1)

    nums2 = [1,2,0]
    expected2 = [0,1,2]
    test('test2', nums2, expected2)


# 给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，
# 使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

# 此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

# 注意:
# 不能使用代码库中的排序函数来解决这道题。

# 示例:

# 输入: [2,0,2,1,1,0]
# 输出: [0,0,1,1,2,2]
# 进阶：

# 一个直观的解决方案是使用计数排序的两趟扫描算法。
# 首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
# 你能想出一个仅使用常数空间的一趟扫描算法吗？