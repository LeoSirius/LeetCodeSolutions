from typing import *


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        for n in nums:
            idx = (n - 1) % len(nums)
            nums[idx] += len(nums)

        res = []
        for i, n in enumerate(nums):
            if n <= len(nums):
                res.append(i + 1)

        return res


def test(test_name, nums, expected):
    res = Solution().findDisappearedNumbers(nums)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    nums1 = [4,3,2,7,8,2,3,1]
    expected1 = [5,6]
    test('test1', nums1, expected1)


# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

# Find all the elements of [1, n] inclusive that do not appear in this array.

# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

