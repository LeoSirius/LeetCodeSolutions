from typing import *

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        maxn, minn = max(nums), min(nums)
        max_gap = 0

        bucket_size = max(1, (maxn - minn) // len(nums) - 1)  # 如果所有数相等，则同大小为1
        buckets = [[] for _ in range((maxn-minn) // bucket_size + 1)]

        for i in range(len(nums)):
            location = (nums[i] - minn) // bucket_size
            buckets[location].append(nums[i])
        
        pre_max = float('inf')
        for i in range(len(buckets)):
            if buckets[i] and pre_max != float('inf'):
                max_gap = max(max_gap, min(buckets[i]) - pre_max)
            if buckets[i]:
                pre_max = max(buckets[i])
        
        return max_gap


def test(test_name, nums, expected):
    res = Solution().maximumGap(nums)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    nums1 = [3,6,9,1]
    expected1 = 3
    test('test1', nums1, expected1)

    nums2 = [10]
    expected2 = 0
    test('test2', nums2, expected2)


# Given an unsorted array, find the maximum difference 
# between the successive elements in its sorted form.

# Return 0 if the array contains less than 2 elements.

# Example 1:

# Input: [3,6,9,1]
# Output: 3
# Explanation: The sorted form of the array is [1,3,6,9], either
#              (3,6) or (6,9) has the maximum difference 3.

# Example 2:

# Input: [10]
# Output: 0
# Explanation: The array contains less than 2 elements, therefore return 0.
# Note:

# You may assume all elements in the array are non-negative integers 
# and fit in the 32-bit signed integer range.

# Try to solve it in linear time/space.

