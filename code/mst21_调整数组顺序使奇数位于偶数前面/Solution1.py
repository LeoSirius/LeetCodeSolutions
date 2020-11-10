from threading import main_thread
from typing import *

class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums)-1
        while l < r:
            while nums[l] % 2 == 1 and l < r:  # 加上后半个条件，防止全奇全偶时越界
                l += 1
            while nums[r] % 2 == 0 and l < r:
                r -= 1
            if l < r:
                nums[l], nums[r] = nums[r], nums[l]

        return nums


def test(test_name, nums, expected_arr):
    res = Solution().exchange(nums)
    if res in expected_arr:
        print(f'{test_name} success.')
    else:
        print(f'{test_name} failed.')


if __name__ == "__main__":
    nums1 = [1,2,3,4]
    expected_arr1 = [[1,3,2,4], [3,1,2,4]]
    test('test1', nums1, expected_arr1)

    nums2 = [1,3,5]
    expected_arr2 = [[1,3,5]]
    test('test2', nums2, expected_arr2)



# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，
# 所有偶数位于数组的后半部分。

# 示例：

# 输入：nums = [1,2,3,4]
# 输出：[1,3,2,4] 
# 注：[3,1,2,4] 也是正确的答案之一。
#  

# 提示：

# 1 <= nums.length <= 50000
# 1 <= nums[i] <= 10000


