from typing import *
from collections import defaultdict


class Solution:
    def pairSums(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        mp = defaultdict(int)

        for n in nums:
            n2find = target - n
            if mp[n2find] > 0:
                res.append([n, n2find])
                mp[n2find] -= 1
            else:
                mp[n] += 1

        return res


def test(test_name, nums, target, expected):
    res = Solution().pairSums(nums, target)
    res = [sorted(item) for item in res]
    res.sort()
    expected = [sorted(item) for item in expected]
    expected.sort()
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    nums1 = [5,6,5]
    target1 = 11
    expected1 = [[5,6]]
    test('test1', nums1, target1, expected1)

    nums2 = [5,6,5,6]
    target2 = 11
    expected2 = [[5,6],[5,6]]
    test('test2', nums2, target2, expected2)

