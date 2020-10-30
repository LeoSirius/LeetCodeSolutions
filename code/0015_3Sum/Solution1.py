from typing import *

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for start in range(len(nums)):
            if start > 0 and nums[start] == nums[start-1]:
                continue
            l, r = start + 1, len(nums) - 1
            while l < r:
                s = nums[start] + nums[l] + nums[r]
                if s == 0:
                    res.append([nums[start], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]: l += 1
                    while l < r and nums[r] == nums[r+1]: r -= 1
                elif s < 0:
                    l += 1
                    
                else:
                    r -= 1

        return res


def test(test_name, nums, expected):
    res = Solution().threeSum(nums)
    res = [item.sort() for item in res]
    expected = [item.sort() for item in expected]
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    nums1 = [-1, 0, 1, 2, -1, -4]
    expected1 = [
        [-1, 0, 1],
        [-1, -1, 2]
    ]
    test('test1', nums1, expected1)