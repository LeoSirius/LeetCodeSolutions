from typing import *
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda i:i[0])
        hp = [intervals[0][1]]
        for i in range(1, len(intervals)):
            if hp[0] <= intervals[i][0]:
                heapq.heappop(hp)
            heapq.heappush(hp, intervals[i][1])
        return len(hp)


def test(test_name, intervals, expected):
    res = Solution().minMeetingRooms(intervals)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    intervals1 = [[0, 30],[5, 10],[15, 20]]
    expected1 = 2
    test('test1', intervals1, expected1)

    intervals2 = [[7,10],[2,4]]
    expected2 = 1
    test('test2', intervals2, expected2)

    intervals3 = []
    expected3 = 0
    test('test3', intervals3, expected3)

    intervals4 = [[2,15],[36,45],[9,29],[16,23],[4,9]]
    expected4 = 2
    test('test4', intervals4, expected4)


# Given an array of meeting time intervals consisting of
# start and end times [[s1,e1],[s2,e2],...] (si < ei),
# find the minimum number of conference rooms required.
#
# Example 1:
#
# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2

# Example 2:
#
# Input: [[7,10],[2,4]]
# Output: 1