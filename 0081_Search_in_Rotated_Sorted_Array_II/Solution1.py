from typing import *

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1

        while l <= r:
            while l < r and nums[l] == nums[l+1]: l += 1
            while l < r and nums[r] == nums[r-1]: r -= 1
            m = l + (r - l) // 2
            if target == nums[m]:
                return True

            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            if nums[m] <= nums[r]:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return False


def test(test_name, nums, target, expected):
    res = Solution().search(nums, target)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    nums1 = [2,5,6,0,0,1,2]
    target1 = 0
    expected1 = True
    test('test1', nums1, target1, expected1)

    nums2 = [2,5,6,0,0,1,2]
    target2 = 3
    expected2 = False
    test('test2', nums2, target2, expected2)
