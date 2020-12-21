from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos = 0, 0  # 分别表示余数三种状态的第二位和第一位
        for num in nums:
            ones = ones ^ num & ~twos
            twos = twos ^ num & ~ones

        # 计算完之后，twos全部都是0
        # ones就是最后的答案
        # 因为3个1再模3就没有了，剩下的单个的1都在ones里，就是最后的结果
        return ones

def test(test_name, nums, expected):
    res = Solution().singleNumber(nums)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == "__main__":
    nums1 = [3,4,3,3]
    expected1 = 4
    test('test1', nums1, expected1)

    nums2 = [9,1,7,9,7,9,7]
    expected2 = 1
    test('test2', nums2, expected2)

# 在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。

# 示例 1：
# 输入：nums = [3,4,3,3]
# 输出：4

# 示例 2：
# 输入：nums = [9,1,7,9,7,9,7]
# 输出：1
#  

# 限制：

# 1 <= nums.length <= 10000
# 1 <= nums[i] < 2^31
