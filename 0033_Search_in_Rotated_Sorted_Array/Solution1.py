from typing import *

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid

            # e.g. 3 4 5 6 7 0 1 2
            # 左半有序，在[l, pivot]内部进行二分查找，右半同理
            # 注意这时 mid < pivot 哦
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            if nums[mid] <= nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1


def test(test_name, nums, target, expected):
    res = Solution().search(nums, target)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    nums1 = [4,5,6,7,0,1,2]
    target1 = 0
    expected1 = 4
    test('test1', nums1, target1, expected1)

    nums2 = [4,5,6,7,0,1,2]
    target2 = 3
    expected2 = -1
    test('test2', nums2, target2, expected2)

    nums3 = [1]
    target3 = 0
    expected3 = -1
    test('test3', nums3, target3, expected3)
