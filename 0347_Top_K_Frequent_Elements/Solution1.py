from typing import *
from collections import defaultdict, Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums) # Counter 是dict子类，值就是出现的次数
        return heapq.nlargest(k, count.keys(), key=count.get) 

def test(test_name, nums, k, expected):
    res = Solution().topKFrequent(nums, k)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    nums1 = [1,1,1,2,2,3]
    k1 = 2
    expected1 = [1,2]
    test('test1', nums1, k1, expected1)

    nums2 = [1]
    k2 = 1
    expected2 = [1]
    test('test2', nums2, k2, expected2)


# Given a non-empty array of integers, return the k most frequent elements.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

# Note:

# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's' time complexity must be better than O(n log n), 
# where n is the array's size.
# It's' guaranteed that the answer is unique, in other words the set 
# of the top k frequent elements is unique.
# You can return the answer in any order.

