from typing import *


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        total = sum(nums)

        for i in range(len(nums)):
            if left_sum == total - left_sum - nums[i]:
                return i
            left_sum += nums[i]

        return -1


def test(test_name, nums, expected):
    res = Solution().pivotIndex(nums)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    nums1 = [1,7,3,6,5,6]
    expected1 = 3
    test('test1', nums1, expected1)

    nums2 = [1,2,3]
    expected2 = -1
    test('test2', nums2, expected2)



# Given an array of integers nums, write a method that returns 
# the "pivot" index of this array.

# We define the pivot index as the index where the sum of all the 
# numbers to the left of the index is equal to the sum of all the 
# numbers to the right of the index.

# If no such index exists, we should return -1. If there are multiple
#  pivot indexes, you should return the left-most pivot index.

#  

# Example 1:

# Input: nums = [1,7,3,6,5,6]
# Output: 3
# Explanation:
# The sum of the numbers to the left of index 3 (nums[3] = 6) is
#  equal to the sum of numbers to the right of index 3.
# Also, 3 is the first index where this occurs.
# Example 2:

# Input: nums = [1,2,3]
# Output: -1
# Explanation:
# There is no index that satisfies the conditions in the problem statement.
#  

# Constraints:

# The length of nums will be in the range [0, 10000].
# Each element nums[i] will be an integer in the range [-1000, 1000].

