from typing import *

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = 0, 0
        for n in nums:
            if count == 0:
                res, count = n, 1
            else:
                if res == n:
                    count += 1
                else:
                    count -= 1
        return res

def test(test_name, nums, expected):
    res = Solution().majorityElement(nums)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    nums1 = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    expected1 = 2
    test('test1', nums1, expected1)


# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。

# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。

# 示例 1:

# 输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
# 输出: 2

# 限制：

# 1 <= 数组长度 <= 50000