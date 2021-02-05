from typing import *
import heapq

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        minhp, maxhp = [], []

        # 初始化两个堆，即处理第一个窗口的情况
        for i in range(k):
            heapq.heappush(minhp, (nums[i], i))
        for i in range(k // 2):
            n, idx = heapq.heappop(minhp)
            heapq.heappush(maxhp, (-n, idx))
        
        res = []
        if k % 2 == 0:
            res.append((minhp[0][0] - maxhp[0][0]) / 2)
        else:
            res.append(float(minhp[0][0]))

        for i in range(k, len(nums)):
            # 新元素小于X，放在最大堆中
            if nums[i] < minhp[0][0]:
                heapq.heappush(maxhp, (-nums[i], i))
                # 如果最左边的元素应该在最小堆中，则调整
                if nums[i-k] >= minhp[0][0]:
                    n, idx = heapq.heappop(maxhp)
                    heapq.heappush(minhp, (-n, idx))
            
            else:
                heapq.heappush(minhp, (nums[i], i))
                # 如果要弹出的元素应该在最大堆中，则调整
                if nums[i-k] <= minhp[0][0]:
                    n, idx = heapq.heappop(minhp)
                    heapq.heappush(maxhp, (-n, idx))

            # 将两个堆在窗口外的元素弹出
            while minhp and minhp[0][1] <= i - k:
                heapq.heappop(minhp)
            while maxhp and maxhp[0][1] <= i - k:
                heapq.heappop(maxhp)

            if k % 2 == 0:
                res.append((minhp[0][0] - maxhp[0][0]) / 2)
            else:
                res.append(float(minhp[0][0]))

        return res


def test(test_name, nums, k, expected):
    res = Solution().medianSlidingWindow(nums, k)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    nums1 = [1,3,-1,-3,5,3,6,7]
    k1 = 3
    expected1 = [1,-1,-1,3,5,6]
    test('test1', nums1, k1, expected1)

    nums2 = [1,2]
    k2 = 1
    expected2 = [1, 2]
    test('test2', nums2, k2, expected2)


# Median is the middle value in an ordered integer list. 
# If the size of the list is even, there is no middle value.
#  So the median is the mean of the two middle value.

# Examples:
# [2,3,4] , the median is 3

# [2,3], the median is (2 + 3) / 2 = 2.5

# Given an array nums, there is a sliding window of size k which is
#  moving from the very left of the array to the very right. 
#  You can only see the k numbers in the window. Each time the 
#  sliding window moves right by one position. Your job is to output
#   the median array for each window in the original array.

# For example,
# Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

# Window position                Median
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       1
#  1 [3  -1  -3] 5  3  6  7       -1
#  1  3 [-1  -3  5] 3  6  7       -1
#  1  3  -1 [-3  5  3] 6  7       3
#  1  3  -1  -3 [5  3  6] 7       5
#  1  3  -1  -3  5 [3  6  7]      6
# Therefore, return the median sliding window as [1,-1,-1,3,5,6].

# Note: 
# You may assume k is always valid, ie: k is always smaller than input
#  array's size for non-empty array.
# Answers within 10^-5 of the actual value will be accepted as correct.

