from typing import *

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) < 2:
            return 0
        intervals.sort(key=lambda pair: pair[1])
        count = 0
        right_bound = intervals[0][1]
        for i in range(1, len(intervals)):
            if right_bound > intervals[i][0]:
                count += 1
                continue
            right_bound = intervals[i][1]
        return count


def test(test_name, intervals, expected):
    res = Solution().eraseOverlapIntervals(intervals)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    intervals1 = [ [1,2], [2,3], [3,4], [1,3] ]
    expected1 = 1
    test('test1', intervals1, expected1)

    intervals2 = [ [1,2], [1,2], [1,2] ]
    expected2 = 2
    test('test2', intervals2, expected2)

    intervals3 = [ [1,2], [2,3] ]
    expected3 = 0
    test('test3', intervals3, expected3)

    intervals4 = []
    expected4 = 0
    test('test4', intervals4, expected4)

    intervals5 = [[1,100],[11,22],[1,11],[2,12]]
    expected5 = 2
    test('test5', intervals5, expected5)


# 给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。

# 注意:

# 可以认为区间的终点总是大于它的起点。
# 区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。
# 示例 1:

# 输入: [ [1,2], [2,3], [3,4], [1,3] ]

# 输出: 1

# 解释: 移除 [1,3] 后，剩下的区间没有重叠。


# 输入: [ [1,2], [1,2], [1,2] ]

# 输出: 2

# 解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。

# 示例 3:

# 输入: [ [1,2], [2,3] ]

# 输出: 0

# 解释: 你不需要移除任何区间，因为它们已经是无重叠的了。

