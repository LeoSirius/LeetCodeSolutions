from typing import *

from functools import cmp_to_key

class Solution:
    def minNumber(self, nums: List[int]) -> str:
        def cmp(a, b):
            # returns a negative number for less-than, zero for equality, 
            # or a positive number for greater-than.

            # 如果a+b小于b+a，返回负数，说明a应该小于b，说明a在b前面。这正好是我们想要的结果
            return int(a+b) - int(b+a)

        nums_str = [str(i) for i in nums]
        nums_str.sort(key=cmp_to_key(cmp))
        return ''.join(nums_str)
        

def test(test_name, nums, expected):
    res = Solution().minNumber(nums)
    print('res = ' + res)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    nums1 = [10,2]
    expected1 = "102"
    test('test1', nums1, expected1)

    nums2 = [3,30,34,5,9]
    expected2 = "3033459"
    test('test2', nums2, expected2)


# 输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。

# 示例 1:
# 输入: [10,2]
# 输出: "102"

# 示例 2:
# 输入: [3,30,34,5,9]
# 输出: "3033459"

# 提示:
# 0 < nums.length <= 100

# 说明:
# 输出结果可能非常大，所以你需要返回一个字符串而不是整数
# 拼接起来的数字可能会有前导 0，最后结果不需要去掉前导 0
