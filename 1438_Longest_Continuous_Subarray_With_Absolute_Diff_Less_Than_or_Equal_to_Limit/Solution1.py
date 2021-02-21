from typing import *
import heapq
from collections import Counter


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        window = Counter()
        window_min, window_max = nums[0], nums[0]
        l, r = 0, 0
        res = 0

        while r < len(nums):
            window[nums[r]] += 1
            window_min = min(window_min, nums[r])
            window_max = max(window_max, nums[r])
            while len(window.keys()) > 1 and window_max - window_min > limit:
                window[nums[l]] -= 1
                window = Counter({k: v for k, v in window.items() if v > 0})
                l += 1
                window_min = min(window.keys())
                window_max = max(window.keys())
            res = max(res, r + 1 - l)
            r += 1

        return res



def test(test_name, nums, limit, expected):
    res = Solution().longestSubarray(nums, limit)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    nums1 = [8,2,4,7]
    limit1 = 4
    expected1 = 2
    test('test1', nums1, limit1, expected1)

    nums2 = [10,1,2,4,7,2]
    limit2 = 5
    expected2 = 4
    test('test2', nums2, limit2, expected2)

    nums3 = [4,2,2,2,4,4,2,2]
    limit3 = 0
    expected3 = 3
    test('test3', nums3, limit3, expected3)

