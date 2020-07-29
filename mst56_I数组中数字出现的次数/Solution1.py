from typing import *

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for i in nums:
            xor ^= i

        idx = 1
        while xor & 1 == 0:
            idx += 1
            xor >>= 1

        r1, r2 = 0, 0
        for i in nums:
            if ((i >> (idx-1)) & 1 == 0):
                r1 ^= i
            else:
                r2 ^= i
        
        return [r1, r2]
            


def test(test_name, nums, expected):
    res = Solution().singleNumber(nums)
    if sorted(res) == sorted(expected):
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    nums1 = [1,2,1,3,2,5]
    expected1 = [3,5]
    test('test1', nums1, expected1)



# Given an array of numbers nums, in which exactly two elements 
# appear only once and all the other elements appear exactly twice. 
# Find the two elements that appear only once.

# Example:

# Input:  [1,2,1,3,2,5]
# Output: [3,5]
# Note:

# The order of the result is not important. 
# So in the above example, [5, 3] is also correct.
# Your algorithm should run in linear runtime complexity.
# Could you implement it using only constant space complexity?
