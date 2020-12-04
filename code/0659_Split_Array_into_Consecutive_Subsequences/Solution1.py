from typing import *
import heapq
from collections import defaultdict

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        chains = defaultdict(list)

        for i in nums:
            if not chains[i-1]:
                # 如果当前这个数的前一个数不在chains中，说明当前这个数就是开头，长度设置为1
                heapq.heappush(chains[i], 1)
            else:
                # 前一个数在chains，前一个数最短的那个列不再作为结尾，pop出。push当前数i，并作为结尾，更新长度
                min_len = heapq.heappop(chains[i-1])
                heapq.heappush(chains[i], min_len + 1)
        
        # 注意chains本身不是最小堆，chains的值list才是最小堆。所以第一个元素必然是最短的
        for k, chain in chains.items():
            if chain and chain[0] < 3:
                return False
        
        return True


def test(test_name, nums, expected):
    res = Solution().isPossible(nums)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    nums1 = [1,2,3,3,4,5]
    expected1 = True
    test('test1', nums1, expected1)

    nums2 = [1,2,3,3,4,4,5,5]
    expected2 = True
    test('test2', nums2, expected2)

    nums3 = [1,2,3,4,4,5]
    expected3 = False
    test('test3', nums3, expected3)

    nums4 = [1,2,3,3]
    expected4 = False
    test('test4', nums4, expected4)


# 给你一个按升序排序的整数数组 num（可能包含重复数字），
# 请你将它们分割成一个或多个子序列，其中每个子序列都由连续整数组成且长度至少为 3 。

# 如果可以完成上述分割，则返回 true ；否则，返回 false 。

#  

# 示例 1：

# 输入: [1,2,3,3,4,5]
# 输出: True
# 解释:
# 你可以分割出这样两个连续子序列 : 
# 1, 2, 3
# 3, 4, 5
#  

# 示例 2：

# 输入: [1,2,3,3,4,4,5,5]
# 输出: True
# 解释:
# 你可以分割出这样两个连续子序列 : 
# 1, 2, 3, 4, 5
# 3, 4, 5
#  

# 示例 3：

# 输入: [1,2,3,4,4,5]
# 输出: False
#  

# 提示：

# 输入的数组长度范围为 [1, 10000]

