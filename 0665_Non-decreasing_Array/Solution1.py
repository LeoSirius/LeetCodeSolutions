from typing import *

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        cnt = 0

        for i in range(1, len(nums)):
            # 需要单调递增（不用严格）<=是满足条件的，>是不满足的
            if nums[i-1] > nums[i]:
                cnt += 1

                # 下面即是把不满足的两个数改为相等，具体改那个数有三种情况
                # i-1 = 0，则改第一个数，为了i不影响后面的
                if i == 1:
                    nums[i-1] = nums[i]
                # 尽量让 i-2 <= i-1 < i。这时能改i-1，就不要改i
                elif i == 1 or nums[i] >= nums[i-2]:
                    nums[i-1] = nums[i]
                # 这时 i < i-2, i < i-1，    3 4 1 -> 3 4 4
                # 改i-1也没用，改i
                else:
                    nums[i] = nums[i-1]

        return cnt <= 1


def test(test_name, nums, expected):
    res = Solution().checkPossibility(nums)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    nums1 = [4,2,3]
    expected1 = True
    test('test1', nums1, expected1)

    nums2 = [4,2,1]
    expected2 = False
    test('test2', nums2, expected2)



# Given an array nums with n integers, your task is to 
# check if it could become non-decreasing by modifying 
# at most one element.

# We define an array is non-decreasing if nums[i] <= nums[i + 1] 
# holds for every i (0-based) such that (0 <= i <= n - 2).

#  

# Example 1:

# Input: nums = [4,2,3]
# Output: true
# Explanation: You could modify the first 4 to 1 to get 
# a non-decreasing array.

# Example 2:

# Input: nums = [4,2,1]
# Output: false
# Explanation: You can't get a non-decreasing array by 
# modify at most one element.
#  

# Constraints:

# n == nums.length
# 1 <= n <= 104
# -105 <= nums[i] <= 105

