from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for n in nums:
            n2find = target - n
            if n2find in d:
                return [n2find, n]
            d[n] = 1


def test(test_name, nums, target, expected):
    res = Solution().twoSum(nums, target)
    if sorted(res) == sorted(expected):
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == "__main__":
    nums1 = [2,7,11,15]
    target1 = 9
    expected1 = [2,7]
    test('test1', nums1, target1, expected1)

    nums2 = [10,26,30,31,47,60]
    target2 = 40
    expected2 = [10, 30]
    test('test2', nums2, target2, expected2)


# 输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。
# 如果有多对数字的和等于s，则输出任意一对即可。

# 示例 1：
# 输入：nums = [2,7,11,15], target = 9
# 输出：[2,7] 或者 [7,2]

# 示例 2：
# 输入：nums = [10,26,30,31,47,60], target = 40
# 输出：[10,30] 或者 [30,10]
#  

# 限制：
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^6
