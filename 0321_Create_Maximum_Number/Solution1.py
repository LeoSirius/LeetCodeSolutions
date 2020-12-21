from typing import *

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        
        def pick_max(nums, k):
            # 这个函数就是一个数组nums，k的情况
            # 这个函数选出nums中按顺序的k个数能组成的最大数

            # 遍历每一个数放到栈中，如果新的数大于栈顶的数，则pop出前面那个小的数
            stk = []
            drop_cnt = len(nums) - k
            for n in nums:
                while drop_cnt and stk and stk[-1] < n:
                    stk.pop()
                    drop_cnt -= 1
                stk.append(n)
            return stk[:k]

        def merge(A, B):
            # 这个函数返回A和B两个数在保留所有数的情况下，按顺序能组成的最大数
            res = []
            while A or B:
                bigger = A if A > B else B  # 两个list比，就是比较第一个不同的数的大小
                res.append(bigger[0])
                bigger.pop(0)

            return res

        res_list = []
        for i in range(k+1):
            # i从0到k，k-i从k到0
            # i + k - i == k，即两个数组中各自取的数的个数加起来就是k
            if i <= len(nums1) and k-i <= len(nums2):
                res_list.append(merge(pick_max(nums1, i), pick_max(nums2, k-i)))

        return max(res_list)


def test(test_name, nums1, nums2, k, expected):
    res = Solution().maxNumber(nums1, nums2, k)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    nums11 = [3, 4, 6, 5]
    nums21 = [9, 1, 2, 5, 8, 3]
    k1 = 5
    expected1 = [9, 8, 6, 5, 3]
    test('test1', nums11, nums21, k1, expected1)

    nums12 = [6, 7]
    nums22 = [6, 0, 4]
    k2 = 5
    expected2 = [6, 7, 6, 0, 4]
    test('test2', nums12, nums22, k2, expected2)

    nums13 = [3, 9]
    nums23 = [8, 9]
    k3 = 3
    expected3 = [9, 8, 9]
    test('test3', nums13, nums23, k3, expected3)


# Given two arrays of length m and n with digits 0-9 representing two numbers. 
# Create the maximum number of length k <= m + n from digits of the two. 
# The relative order of the digits from the same array must be preserved. 
# Return an array of the k digits.

# Note: You should try to optimize your time and space complexity.

# Example 1:

# Input:
# nums1 = [3, 4, 6, 5]
# nums2 = [9, 1, 2, 5, 8, 3]
# k = 5
# Output:
# [9, 8, 6, 5, 3]

# Example 2:

# Input:
# nums1 = [6, 7]
# nums2 = [6, 0, 4]
# k = 5
# Output:
# [6, 7, 6, 0, 4]

# Example 3:

# Input:
# nums1 = [3, 9]
# nums2 = [8, 9]
# k = 3
# Output:
# [9, 8, 9]
