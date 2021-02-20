from typing import *
import collections


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left, right = {}, {}
        counter = collections.Counter()

        for i, num in enumerate(nums):
            if num not in left:
                left[num] = i
            right[num] = i
            counter[num] += 1

        deg = max(counter.values())
        res = len(nums)

        for k, v in counter.items():
            if v == deg:
                res = min(res, right[k] + 1 - left[k])

        return res


def test(test_name, nums, expected):
    res = Solution().findShortestSubArray(nums)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    nums1 = [1,2,2,3,1]
    expected1 = 2
    test('test1', nums1, expected1)

    nums2 = [1,2,2,3,1,4,2]
    expected2 = 6
    test('test2', nums2, expected2)

