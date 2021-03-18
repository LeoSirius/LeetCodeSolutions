from typing import *

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        tail = 0
        p = 0
        while p < len(nums):
            if nums[p] != val:
                nums[tail] = nums[p]
                tail += 1
            p += 1

        return tail


def test(test_name, nums, val, expected):
    res = Solution().removeElement(nums, val)
    if nums[:res] == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    nums1 = [3,2,2,3]
    val1 = 3
    expected1 = [2,2]
    test('test1', nums1, val1, expected1)

    nums2 = [0,1,2,2,3,0,4,2]
    val2 = 2
    expected2 = [0,1,3,0,4]
    test('test2', nums2, val2, expected2)
