from typing import *

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for n in nums:
            if count == 0:
                candidate = n
            count += (1 if n == candidate else -1)
        return candidate


def test(test_name, nums, expected):
    res = Solution().majorityElement(nums)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    nums1 = [3,2,3]
    expected1 = 3
    test("test1", nums1, expected1)

    nums2 = [2,2,1,1,1,2,2]
    expected2 = 2
    test("test2", nums2, expected2)


# Given an array of size n, find the majority element.
# The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority
# element always exist in the array.

# Example 1:

# Input: [3,2,3]
# Output: 3

# Example 2:

# Input: [2,2,1,1,1,2,2]
# Output: 2

