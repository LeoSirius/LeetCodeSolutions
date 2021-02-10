from typing import *

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]]
        res = dp[-1]

        for i in range(1, len(nums)):
            dp.append(max(dp[-1] + nums[i], nums[i]))
            res = max(res, dp[-1])

        return res


def test(test_name, nums, expected):
    res = Solution().maxSubArray(nums)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    nums1 = [-2,1,-3,4,-1,2,1,-5,4]
    expected1 = 6
    test('test1', nums1, expected1)


# You are given an array of integers (both positive and negative). 
# Find the contiguous sequence with the largest sum. 
# Return the sum.

# Example:

# Input:  [-2,1,-3,4,-1,2,1,-5,4]
# Output:  6
# Explanation:  [4,-1,2,1] has the largest sum 6.
# Follow Up:

# If you have figured out the O(n) solution, try 
# coding another solution using the divide and conquer approach,
#  which is more subtle.

