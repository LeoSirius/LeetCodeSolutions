from typing import *

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def get_right_border(target):
            l, r = 0, len(nums) - 1
            while l <= r:
                # 其实是三种情况
                # mid == target: left + 1
                # mid < target: left + 1
                # target < mid: right - 1

                # 后面两种情况很好理解。
                # 因为是查找右边界（第一个大于target的数）
                # 所以当等于target的时候，left也加1，就行
                mid = l + (r - l) // 2
                if nums[mid] <= target:
                    l += 1
                else:
                    r -= 1
            return l

        # 如5,7,7,8,8,10
        # helper(target) 返回的是10的索引
        # helper(target - 1) 返回的是第一个8的索引
        # 即helper返回target后面第一个数的索引
        # 即helper返回target的右边界
        return get_right_border(target) - get_right_border(target - 1)


def test(test_name, nums, target, expected):
    res = Solution().search(nums, target)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    nums1 = [5,7,7,8,8,10]
    target1 = 8
    expected1 = 2
    test('test1', nums1, target1, expected1)

    nums2 = [5,7,7,8,8,10]
    target2 = 6
    expected2 = 0
    test('test2', nums2, target2, expected2)


# 统计一个数字在排序数组中出现的次数。

# 示例 1:

# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: 2

# 示例 2:
# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: 0
#  

# 限制：
# 0 <= 数组长度 <= 50000
