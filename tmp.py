from typing import *

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        pass

def test(test_name, nums, expected):
    res = Solution().isPossible(nums)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    nums1 = [1,2,3,3,4,5]
    expected1 = True
    test('test1', nums1, expected1)

    nums2 = [1,2,3,3,4,4,5,5]
    expected2 = True
    test('test2', nums2, expected2)

    nums3 = [1,2,3,4,4,5]
    expected3 = False
    test('test3', nums3, expected3)


# Given an array nums sorted in ascending order, return 
# true if and only if you can split it into 1 or more subsequences 
# such that each subsequence consists of consecutive integers and has
#  length at least 3.

# Example 1:

# Input: [1,2,3,3,4,5]
# Output: True
# Explanation:
# You can split them into two consecutive subsequences : 
# 1, 2, 3
# 3, 4, 5

# Example 2:

# Input: [1,2,3,3,4,4,5,5]
# Output: True
# Explanation:
# You can split them into two consecutive subsequences : 
# 1, 2, 3, 4, 5
# 3, 4, 5

# Example 3:

# Input: [1,2,3,4,4,5]
# Output: False
#  

# Constraints:

# 1 <= nums.length <= 10000

