from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        def N_sum(N, nums, target, path, res):
            if N < 2 or len(nums) < N or N * nums[0] > target or N * nums[-1] < target:
                return

            if N > 2:
                for i in range(len(nums) - N + 1):
                    if i > 0 and nums[i] == nums[i-1]: continue
                    N_sum(N - 1, nums[i+1:], target - nums[i], path + [nums[i]], res)
                return

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
        N_sum(4, nums, target, [], res)
        return res


def test(test_name, nums, target, expected):
    res = Solution().fourSum(nums, target)
    for item in res:
        item.sort()
    res.sort()
    expected = [sorted(item) for item in expected]
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

    nums2 = [-2,-1,-1,1,1,2,2]
    target2 = 0
    expected2 = [[
        -2,-1,1,2],
        [-1,-1,1,1]]
    test('test2', nums2, target2, expected2)

