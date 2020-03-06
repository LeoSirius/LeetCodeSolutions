from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


def test(test_name, nums, target, expected):
    slt = Solution()
    res = slt.search(nums, target)
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
