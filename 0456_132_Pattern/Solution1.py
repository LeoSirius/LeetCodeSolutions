from typing import *

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        N = len(nums)
        left_min = [float('inf')] * N          # left_min[i] 是对每個元素i，左邊最小的那個數

        for i in range(1, N):
            left_min[i] = min(left_min[i-1], nums[i-1])

        stk = []
        for k in range(N-1, -1, -1):
            numsj = float('-inf')
            # numsj 就是 stk 裡比 k 小的元素
            # 且從右到左遍歷，保證了 numsj 在 nums[k] 的右邊
            while stk and stk[-1] < nums[k]:
                numsj = stk.pop()
            # nums[k] > numsj > left_min[k]
            if left_min[k] < numsj:
                return True
            stk.append(nums[k])

        return False


def test(test_name, nums, expected):
    res = Solution().find132pattern(nums)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    nums1 = [1,2,3,4]
    expected1 = False
    test('test1', nums1, expected1)

    nums2 = [3,1,4,2]
    expected2 = True
    test('test2', nums2, expected2)

    nums3 = [-1,3,2,0]
    expected3 = True
    test('test3', nums3, expected3)
