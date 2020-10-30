from typing import *

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def n_sum(nums, target, N, path, res):
            if len(nums) < N or N < 2 or N * nums[-1] < target or target < N * nums[0]:
                return

            if 2 < N:
                for i in range(len(nums) - N + 1):
                    if i > 0 and nums[i] == nums[i-1]: continue
                    n_sum(nums[i+1:], target - nums[i], N - 1, path + [nums[i]], res)
                return

            # N == 2
            l, r = 0, len(nums) - 1
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    res.append(path + [nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]: l += 1
                    while l < r and nums[r] == nums[r+1]: r -= 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
        
        res = []
        nums.sort()
        n_sum(nums, target, 4, [], res)
        return res

def test(test_name, nums, target, expected):
    res = Solution().fourSum(nums, target)
    for item in res:
        item.sort()
    res.sort()
    for item in expected:
        item.sort()
    expected.sort()
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    nums1 = [1, 0, -1, 0, -2, 2]
    target1 = 0
    expected1 = [
        [-1,  0, 0, 1],
        [-2, -1, 1, 2],
        [-2,  0, 0, 2]
    ]
    test('test1', nums1, target1, expected1)