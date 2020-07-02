from typing import  List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        pass

def test(test_name, nums, expected):
    res = Solution().largestNumber(nums)
    if res == expected:
        print(test_name)

if __name__ == '__main__':
    pass


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
