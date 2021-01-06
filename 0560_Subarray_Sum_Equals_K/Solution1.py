from typing import *

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {}

        pre_sum = 0
        cnt = 0
        dic[0] = 1     # key是presume， value是这个presum的出现次数
        for i in range(len(nums)):
            pre_sum += nums[i]
            if pre_sum - k in dic:
                cnt += dic[pre_sum - k]
            dic[pre_sum] = dic.get(pre_sum, 0) + 1

        return cnt


def test(test_name, nums, k, expected):
    res = Solution().subarraySum(nums, k)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == "__main__":
    nums1 = [1,1,1]
    k1 = 2
    expected1 = 2
    test('test1', nums1, k1, expected1)

    nums2 = [1,2,3]
    k2 = 3
    expected2 = 2
    test('test2', nums2, k2, expected2)


# Given an array of integers nums and an integer k, 
# return the total number of continuous subarrays whose sum equals to k.

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2

# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2

# Constraints:

# 1 <= nums.length <= 2 * 104
# -1000 <= nums[i] <= 1000
# -107 <= k <= 107
