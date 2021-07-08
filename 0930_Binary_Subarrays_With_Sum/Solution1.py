from typing import *
from collections import defaultdict


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        res = 0
        pre_sum = [0] * (len(nums) + 1)
        for i in range(1, len(nums)+1):
            pre_sum[i] = pre_sum[i-1] + nums[i-1]

        mapper = defaultdict(int)
        for i in range(len(nums)+1):
            n2find = pre_sum[i] - goal
            res += mapper[n2find]
            mapper[pre_sum[i]] += 1
        return res


def test(test_name, nums, goal, expected):
    res = Solution().numSubarraysWithSum(nums, goal)
    if type(res) == type(expected) and res == expected:
        print(test_name + ' succeed')
    else:
        print(test_name + ' fail')


if __name__ == '__main__':
    nums1 = [1,0,1,0,1]
    goal1 = 2
    expected1 = 4
    test('test1', nums1, goal1, expected1)

    nums2 = [0,0,0,0,0]
    goal2 = 0
    expected2 = 15
    test('test2', nums2, goal2, expected2)
