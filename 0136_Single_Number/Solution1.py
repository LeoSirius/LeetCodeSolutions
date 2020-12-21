from typing import *

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res ^= n
        return res

def test(test_name, nums, expected):
    res = Solution().singleNumber(nums)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    nums1 = [2,2,1]
    expected1 = 1
    test('test1', nums1, expected1)

    nums2 = [4,1,2,1,2]
    expected2 = 4
    test('test2', nums2, expected2)


# Given a non-empty array of integers, every element appears 
# twice except for one. Find that single one.

# Note:

# Your algorithm should have a linear runtime complexity.
#  Could you implement it without using extra memory?

# Example 1:

# Input: [2,2,1]
# Output: 1
# Example 2:

# Input: [4,1,2,1,2]
# Output: 4
