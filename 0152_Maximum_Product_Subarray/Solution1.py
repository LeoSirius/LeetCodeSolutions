from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        imax = imin = res
        for i in range(1, len(nums)):
            if nums[i] < 0:
                imax, imin = imin, imax
            imax = max(nums[i], nums[i] * imax)
            imin = min(nums[i], nums[i] * imin)
            res = max(res, imax)
        return res


def test(test_name, nums, expected):
    res = Solution().maxProduct(nums)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    nums1 = [2,3,-2,4]
    expected1 = 6
    test('test1', nums1, expected1)

    nums2 = [-2,0,-1]
    expected2 = 0
    test('test2', nums2, expected2)

    nums3 = [-2, 3, -4]
    expected3 = 24
    test('test3', nums3, expected3)
