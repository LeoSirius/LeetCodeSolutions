from typing import List

class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        

def test(test_name, nums):
    res = Solution().singleNumbers(nums)
    if sorted(res) == sorted(nums):
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == "__main__":
    nums1 = [4,1,4,6]
    expected1 = [1,6]
    test('test1', nums1, expected1)

    nums2 = [1,2,10,4,1,4,3,3]
    expected2 = [2,10]
    test('test2', nums2, expected2)


# 一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。
# 要求时间复杂度是O(n)，空间复杂度是O(1)。

# 示例 1：
# 输入：nums = [4,1,4,6]
# 输出：[1,6] 或 [6,1]

# 示例 2：
# 输入：nums = [1,2,10,4,1,4,3,3]
# 输出：[2,10] 或 [10,2]

# 限制：
# 2 <= nums.length <= 10000

