from typing import *

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        pass
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos = 0, 0  # 分别表示余数三种状态的第二位和第一位
        for num in nums:
            ones = ones ^ num & ~twos
            twos = twos ^ num & ~ones

        # 计算完之后，twos全部都是0
        # ones就是最后的答案
        # 因为3个1再模3就没有了，剩下的单个的1都在ones里，就是最后的结果
        return ones

def test(test_name, nums, expected):
    res = Solution().singleNumber(nums)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    nums1 = [2,2,3,2]
    expected1 = 3
    test("test1", nums1, expected1)

    nums2 = [0,1,0,1,0,1,99]
    expected2 = 99
    test("test2", nums2, expected2)


# Given a non-empty array of integers, every element appears 
# three times except for one, which appears exactly once. 
# Find that single one.

# Note:

# Your algorithm should have a linear runtime complexity. 
# Could you implement it without using extra memory?

# Example 1:

# Input: [2,2,3,2]
# Output: 3

# Example 2:

# Input: [0,1,0,1,0,1,99]
# Output: 99