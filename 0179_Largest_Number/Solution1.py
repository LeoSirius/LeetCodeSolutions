from functools import cmp_to_key
from typing import  List

class Solution:
    def cmp(self, a, b):
        # python 自定义cmp函数不是返回true false，而是返回 整数，负数和0
        return int(b + a) - int(a + b)

    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(n) for n in nums]
        nums.sort(key=cmp_to_key(self.cmp))
        res = ''.join(nums)
        return '0' if res[0] == '0' else res


def test(test_name, nums, expected):
    res = Solution().largestNumber(nums)
    print('res = {}'.format(res))
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == '__main__':
    nums1 = [10, 2]
    expected1 = '210'
    test('test1', nums1, expected1)

    nums2 = [3,30,34,5,9]
    expected2 = "9534330"
    test('test2', nums2, expected2)

    nums3 = [0,0]
    expected3 = '0'
    test('test3', nums3, expected3)


# Given a list of non negative integers, arrange them such that they
# form the largest number.
#
# Example 1:
#
# Input: [10,2]
# Output: "210"

# Example 2:
# Input: [3,30,34,5,9]
# Output: "9534330"

# Note: The result may be very large, so you need to return a string
# instead of an integer.
