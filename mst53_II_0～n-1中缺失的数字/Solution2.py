from typing import *

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == mid:
                l += 1
            else:
                r -= 1
        return l


def test(test_name, nums, expected):
    res = Solution().missingNumber(nums)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    nums1 = [0,1,3]
    expected1 = 2
    test('test1', nums1, expected1)

    nums2 = [0,1,2,3,4,5,6,7,9]
    expected2 = 8
    test('test2', nums2, expected2)

    nums3 = [0]
    expected3 = 1
    test('test3', nums3, expected3)

    nums4 = [1]
    expected4 = 0
    test('test4', nums4, expected4)


# 一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。
# 在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。

# 示例 1:

# 输入: [0,1,3]
# 输出: 2

# 示例 2:
# 输入: [0,1,2,3,4,5,6,7,9]
# 输出: 8
#  

# 限制：
# 1 <= 数组长度 <= 10000
