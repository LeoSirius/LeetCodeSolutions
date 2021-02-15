from typing import *


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        start = -1

        for i, v in enumerate(nums):
            if v == 1:
                res = max(res, i - start)
            else:
                start = i

        return res


def test(test_name, nums, expected):
    res = Solution().findMaxConsecutiveOnes(nums)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    nums1 = [1,1,0,1,1,1]
    expected1 = 3
    test('test1', nums1, expected1)


# Given a binary array, find the maximum number of consecutive 1s in this array.

# Example 1:

# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s.
#     The maximum number of consecutive 1s is 3.
# Note:

# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000

