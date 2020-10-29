from typing import *

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = []
        res = []

        for i in range(len(nums)):

            while dq and nums[dq[-1]] <= nums[i]:
                dq = dq[:-1]
            
            if dq and dq[0] < i + 1 - k:
                dq = dq[1:]
            
            dq.append(i)

            if i >= k - 1:
                res.append(nums[dq[0]])

        return res


def test(test_name, nums, k, expected):
    res = Solution().maxSlidingWindow(nums, k)
    if res == expected:
        print(f'{test_name} success.')
    else:
        print(f'{test_name} failed.')


if __name__ == "__main__":
    nums1 = [1,3,-1,-3,5,3,6,7]
    k1 = 3
    expected1 = [3,3,5,5,6,7]
    test('test1', nums1, k1, expected1)



# 给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。

# 示例:

# 输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
# 输出: [3,3,5,5,6,7] 
# 解释: 

#   滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
#  

# 提示：

# 你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。

