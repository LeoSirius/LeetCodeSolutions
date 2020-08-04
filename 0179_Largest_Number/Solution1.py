from typing import *
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(a, b):
            # 如果是整数，则b排在a后面
            # 这里如果b+a > a+b，则b排在后面
            # a = 30, b = 3
            # 330 - 303 > 0
            # b排在前面，结果就是330
            return int(b+a) - int(a+b)

        nums = [str(n) for n in nums]
        nums.sort(key=cmp_to_key(cmp))

        return '0' if nums[0] == '0' else ''.join(nums)


def test(test_name, nums, expected):
    res = Solution().largestNumber(nums)
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
