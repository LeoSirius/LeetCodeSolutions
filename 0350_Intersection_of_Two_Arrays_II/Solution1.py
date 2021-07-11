from typing import *
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1, c2 = Counter(nums1), Counter(nums2)
        res = []
        for k in nums1 + nums2:
            if k in res:
                continue
            if k in c1 and k in c2:
                times = min(c1[k], c2[k])
                res.extend([k] * times)
        return res


def test(test_name, nums1, nums2, expected):
    res = Solution().intersect(nums1, nums2)
    res.sort()
    expected.sort()
    if res == expected:
        print(test_name + ' succeed')
    else:
        print(test_name + ' fail')


if __name__ == "__main__":
    nums11 = [1,2,2,1]
    nums21 = [2,2]
    expected1 = [2,2]
    test('test1', nums11, nums21, expected1)

    nums12 = [4,9,5]
    nums22 = [9,4,9,8,4]
    expected2 = [4,9]
    test('test2', nums12, nums22, expected2)


# 给定两个数组，编写一个函数来计算它们的交集。


# 示例 1：

# 输入：nums1 = [1,2,2,1], nums2 = [2,2]
# 输出：[2,2]

# 示例 2:

# 输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出：[4,9]
#  

# 说明：

# 输出结果中每个元素出现的次数，应与元素在两个数组中出现次数的最小值一致。
# 我们可以不考虑输出结果的顺序。

# 进阶：

# 如果给定的数组已经排好序呢？你将如何优化你的算法？
# 如果 nums1 的大小比 nums2 小很多，哪种方法更优？
# 如果 nums2 的元素存储在磁盘上，内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
