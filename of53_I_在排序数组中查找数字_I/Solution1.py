from typing import *
from collections import Counter

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return Counter(nums)[target]


def test(test_name, nums, target, expected):
    res = Solution().search(nums, target)
    if res == expected:
        print(test_name + ' succeed')
    else:
        print(test_name + ' fail')


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
