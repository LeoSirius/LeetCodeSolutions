from typing import *


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mp = {0:-1}  # 辅助数据，初始情况下在 -1 位置，0 和 1 的 cur = 0
        cur, res = 0, 0

        for i in range(len(nums)):
            if nums[i] == 0:
                cur -= 1
            else:
                cur += 1
            if cur in mp:
                res = max(res, i - mp[cur])
            else:
                mp[cur] = i

        return res


def test(test_name, nums, expected):
    res = Solution().findMaxLength(nums)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    nums1 = [0,1]
    expected1 = 2
    test('test1', nums1, expected1)

    nums2 = [0,1,0]
    expected2 = 2
    test('test2', nums2, expected2) 
