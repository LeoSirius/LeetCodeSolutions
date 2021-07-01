from typing import *


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        _set = set()
        for n in nums:
            if n in _set:
                return True
            _set.add(n)
        return False


def test(test_name, nums, expected):
    res = Solution().containsDuplicate(nums)
    if res == expected:
        print(test_name + ' succeed')
    else:
        print(test_name + ' fail')


if __name__ == "__main__":
    nums1 = [1,2,3,1]
    expected1 = True
    test('test1', nums1, expected1)

    nums2 = [1,2,3,4]
    expected2 = False
    test('test2', nums2, expected2)

    nums3 = [1,1,1,3,3,4,3,2,4,2]
    expected3 = True
    test('test3', nums3, expected3)


# Given an array of integers, find if the array contains any duplicates.

# Your function should return true if any value appears at least twice
# in the array, and it should return false if every element is distinct.

# Example 1:

# Input: [1,2,3,1]
# Output: true
# Example 2:

# Input: [1,2,3,4]
# Output: false
# Example 3:

# Input: [1,1,1,3,3,4,3,2,4,2]
# Output: true

