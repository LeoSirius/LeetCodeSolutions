from typing import *

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = newInterval
        placed = False           # 标识是否加过newInterval
        res = []

        for l, r in intervals:
            # 对每个l，r 有三种情况
            # newInterval 在 [l,r]的左边，加到res里
            # newInterval 在 [l,r]的右边，不管，放到后面处理
            # newInterval 和 [l,r]有交集, 更新newInterval
            if l > end:
                if not placed:
                    res.append([start, end])
                    placed = True
                res.append([l, r])
            
            elif r < start:
                res.append([l, r])

            else:
                start = min(start, l)
                end = max(end, r)

        if not placed:
            res.append([start, end])
        
        return res


def test(test_name, intervals, newInterval, expected):
    res = Solution().insert(intervals, newInterval)
    if res == expected:
        print(f'{test_name} success.')
    else:
        print(f'{test_name} failed.')


if __name__ == "__main__":
    intervals1 = [[1,3],[6,9]]
    newInterval1 = [2,5]
    expected1 = [[1,5],[6,9]]
    test('test1', intervals1, newInterval1, expected1)

    intervals2 = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval2 = [4,8]
    expected2 = [[1,2],[3,10],[12,16]]
    test('test2', intervals2, newInterval2, expected2)

    intervals3 = []
    newInterval3 = [5,7]
    expected3 = [[5,7]]
    test('test3', intervals3, newInterval3, expected3)

    intervals4 = [[1,5]]
    newInterval4 = [2,3]
    expected4 = [[1,5]]
    test('test4', intervals4, newInterval4, expected4)

    intervals5 = [[1,5]]
    newInterval5 = [2,7]
    expected5 = [[1,7]]
    test('test5', intervals5, newInterval5, expected5)

    intervals6 = [[1,5]]
    newInterval6 = [6,8]
    expected6 = [[1,5], [6,8]]
    test('test6', intervals6, newInterval6, expected6)

    intervals7 = [[1,5]]
    newInterval7 = [0,3]
    expected7 = [[0,5]]
    test('test7', intervals7, newInterval7, expected7)

    intervals8 = [[1,5]]
    newInterval8 = [0,0]


# Given a set of non-overlapping intervals, insert a new interval into
#  the intervals (merge if necessary).

# You may assume that the intervals were initially sorted according
#  to their start times.

#  

# Example 1:

# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]

# Example 2:

# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

# Example 3:

# Input: intervals = [], newInterval = [5,7]
# Output: [[5,7]]

# Example 4:

# Input: intervals = [[1,5]], newInterval = [2,3]
# Output: [[1,5]]

# Example 5:

# Input: intervals = [[1,5]], newInterval = [2,7]
# Output: [[1,7]]
#  

# Constraints:

# 0 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= intervals[i][0] <= intervals[i][1] <= 105
# intervals is sorted by intervals[i][0] in ascending order.
# newInterval.length == 2
# 0 <= newInterval[0] <= newInterval[1] <= 105
