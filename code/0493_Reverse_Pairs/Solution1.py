from typing import *

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # 这个函数是求夸A，B的结果，A和B中已经是各自相对排好序的
        def get_reversed(l, r):
            res = 0
            m = l + (r - l) // 2
            j = m + 1
            for i in range(l, m+1):
                while j <= r and nums[i] > nums[j] * 2:
                    res += m+1-i  # nums[i]满足，则[i, mid]中的都满足
                    j += 1
            return res

        def merge_sort(l, r):
            if l >= r:
                return 0
            m = l + (r-l) // 2

            # 先在左右两边里排序，调用get_reversed时，
            # 左右两边已经是各自有序的了
            res = merge_sort(l, m) + merge_sort(m+1, r) + get_reversed(l, r)

            nums_sorted = [0] * (r+1-l) # python的list是动态数组，不是链表，不要用尾增法
            p, i, j = 0, l, m+1

            while i <= m and j <= r:
                if nums[i] <= nums[j]:
                    nums_sorted[p] = nums[i]
                    i += 1
                else:
                    nums_sorted[p] = nums[j]
                    j += 1
                p += 1
            while i <= m:
                nums_sorted[p] = nums[i]
                p += 1
                i += 1
            while j <= r:
                nums_sorted[p] = nums[j]
                p += 1
                j += 1

            # 把排序好的写回原数组
            for i in range(l, r+1):
                nums[i] = nums_sorted[i-l]
                
            return res
        
        res = merge_sort(0, len(nums)-1)

        return res


def test(test_name, nums, expected):
    res = Solution().reversePairs(nums)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == "__main__":
    nums1 = [1,3,2,3,1]
    expected1 = 2
    test('test1', nums1, expected1)

    nums2 = [2,4,3,5,1]
    expected2 = 3
    test('test2', nums2, expected2)

    nums3 = [233,2000000001,234,2000000006,235,2000000003,236,2000000007,237,2000000002,2000000005,233,233,233,233,233,2000000004]
    expected3 = 40
    test('test3', nums3, expected3)


# 给定一个数组 nums ，如果 i < j 且 
# nums[i] > 2*nums[j] 我们就将 (i, j) 称作一个重要翻转对。

# 你需要返回给定数组中的重要翻转对的数量。

# 示例 1:

# 输入: [1,3,2,3,1]
# 输出: 2

# 示例 2:

# 输入: [2,4,3,5,1]
# 输出: 3
# 注意:

# 给定数组的长度不会超过50000。
# 输入数组中的所有数字都在32位整数的表示范围内。
