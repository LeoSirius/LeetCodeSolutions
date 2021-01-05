from typing import *

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return -1


def test(test_name, nums, target, expected):
    res = Solution().search(nums, target)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    nums1 = [-1,0,3,5,9,12]
    target1 = 9
    expected1 = 4
    test('test1', nums1, target1, expected1)

    nums2 = [-1,0,3,5,9,12]
    target2 = 2
    expected2 = -1
    test('test2', nums2, target2, expected2)


# Given a sorted (in ascending order) integer array nums of 
# n elements and a target value, write a function to search target in nums. 
# If target exists, then return its index, otherwise return -1.


# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

# Example 2:

# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
#  

# Note:

# You may assume that all elements in nums are unique.
# n will be in the range [1, 10000].
# The value of each element in nums will be in the range [-9999, 9999].

