from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, val in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                my_sum = nums[i] + nums[l] + nums[r]
                if my_sum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l+1] == nums[l]:
                        l += 1
                    while l < r and nums[r-1] == nums[r]:
                        r -= 1
                    l += 1
                    r -= 1
                elif my_sum > 0:
                    r -= 1
                else:
                    l += 1
        return res


def test(test_name, nums, expected):
    slt = Solution()
    res = slt.threeSum(nums)
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
