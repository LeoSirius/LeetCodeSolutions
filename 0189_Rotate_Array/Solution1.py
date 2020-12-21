from typing import *


def reverse_with_range(nums, start, end):
    # [start, end)
    i, j = start, end-1
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)  # k可能超过Len
        left_len = len(nums)-k
        reverse_with_range(nums, 0, left_len)
        reverse_with_range(nums, left_len, len(nums))
        reverse_with_range(nums, 0, len(nums))


def test(test_name, nums, k, expected):
    Solution().rotate(nums, k)
    if nums == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    nums1 = [1,2,3,4,5,6,7]
    k1 = 3
    expected1 = [5,6,7,1,2,3,4]
    test('test1', nums1, k1, expected1)

    nums2 = [-1,-100,3,99]
    k2 = 2
    expected2 = [3,99,-1,-100]
    test('test2', nums2, k2, expected2)

    nums3 = [1,2,3,4,5,6]
    k3 = 11
    expected3 = [2,3,4,5,6,1]
    test('test3', nums3, k3, expected3)


# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

# 示例 1:

# 输入: [1,2,3,4,5,6,7] 和 k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]

# 示例 2:

# 输入: [-1,-100,3,99] 和 k = 2
# 输出: [3,99,-1,-100]
# 解释: 
# 向右旋转 1 步: [99,-1,-100,3]
# 向右旋转 2 步: [3,99,-1,-100]

# 说明:

# 尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
# 要求使用空间复杂度为 O(1) 的 原地 算法。


