from typing import *

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        presum = [nums[0]]
        for i in range(1, k):
            presum.append(presum[-1] + nums[i])
    
        res = presum[-1] / k
        for i in range(k, len(nums)):
            presum.append(presum[-1] + nums[i])
            sum_of_k = presum[-1] - presum[i-k]
            res = max(res, sum_of_k / k)

        return res


def test(test_name, nums, k, expected):
    res = Solution().findMaxAverage(nums, k)
    if abs(res-expected) <= 0.0001:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    nums1 = [1,12,-5,-6,50,3]
    k1 = 4
    expected1 = 12.75
    test('test1', nums1, k1, expected1)

    nums2 = [0,1,1,3,3]
    k2 = 4
    expected2 = 2.0
    test('test2', nums2, k2, expected2)

    nums3 = [3,3,4,3,0]
    k3 = 3
    expected3 = 3.33333
    test('test3', nums3, k3, expected3)


# Given an array consisting of n integers, find the contiguous 
# subarray of given length k that has the maximum average value.
#  And you need to output the maximum average value.

# Example 1:

# Input: [1,12,-5,-6,50,3], k = 4
# Output: 12.75
# Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75

# Note:

# 1 <= k <= n <= 30,000.
# Elements of the given array will be in the range [-10,000, 10,000].

