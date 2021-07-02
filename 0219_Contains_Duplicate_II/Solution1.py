from typing import *

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp = {}
        for i, v in enumerate(nums):
            if v in mp and i - mp[v] <= k:
                return True
            mp[v] = i

        return False


def test(test_name, nums, k, expected):
    res = Solution().containsNearbyDuplicate(nums, k)
    if res == expected:
        print(test_name + ' succeed')
    else:
        print(test_name + ' fail')


if __name__ == '__main__':
    nums1 = [1,2,3,1]
    k1 = 3
    expected1 = True
    test('test1', nums1, k1, expected1)

    nums2 = [1,0,1,1]
    k2 = 1
    expected2 = True
    test('test2', nums2, k2, expected2)

    nums3 = [1,2,3,1,2,3]
    k3 = 2
    expected3 = False
    test('test3', nums3, k3, expected3)
