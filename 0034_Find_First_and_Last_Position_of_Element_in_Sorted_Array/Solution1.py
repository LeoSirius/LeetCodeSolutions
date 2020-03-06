from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        def b_search_left(nums, target):
            l, r = 0, len(nums) - 1
            while l < r:
                m = l + (r - l) // 2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m
            return l if nums[l] == target else -1
        
        def b_search_right(nums, target):
            l, r = 0, len(nums) - 1
            while l < r:
                m = l + (r - l) // 2 + 1
                if target < nums[m]:
                    r = m - 1
                else:
                    l = m
            return r if nums[r] == target else -1
        
        return [b_search_left(nums, target), b_search_right(nums, target)]


def test(test_name, nums, target, expected):
    res = Solution().searchRange(nums, target)
    print('res = {}'.format(res))
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    nums1 = [5,7,7,8,8,10]
    target1 = 8
    expected1 = [3,4]
    test('test1', nums1, target1, expected1)

    nums2 = [5,7,7,8,8,10]
    target2 = 6
    expected2 = [-1, -1]
    test('test2', nums2, target2, expected2)
