from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i, _ in enumerate(nums):
            if i > 0 and nums[i-1] == nums[i]: continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j-1] == nums[j]: continue
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    my_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if my_sum == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left+1] == nums[left]: left += 1
                        while left < right and nums[right-1] == nums[right]: right -= 1
                        left += 1
                        right -= 1
                    elif my_sum > target:
                        right -= 1
                    else:
                        left += 1
        return res

def test(test_name, nums, target, expected):
    slt = Solution()
    res = slt.fourSum(nums, target)
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

    nums2 = [-2,-1,-1,1,1,2,2]
    target2 = 0
    expected2 = [
        [-2,-1,1,2],
        [-1,-1,1,1]
    ]
    test('test2', nums2, target2, expected2)