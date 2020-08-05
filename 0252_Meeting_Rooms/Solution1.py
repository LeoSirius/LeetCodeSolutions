from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda i:i[0])
        for i in range(len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        return True


def test(test_name, intervals, expected):
    res = Solution().canAttendMeetings(intervals)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    intervals1 = [[0,30],[5,10],[15,20]]
    expected1 = False
    test('test1', intervals1, expected1)

    intervals2 = [[7,10],[2,4]]
    expected2 = True
    test('test2', intervals2, expected2)

    intervals3 = [[13,15],[1,13]]
    expected3 = True
    test('test3', intervals3, expected3)


# Given an array of meeting time intervals consisting of
# start and end times [[s1,e1],[s2,e2],...] (si < ei),
# determine if a person could attend all meetings.
#
# Example 1:
#
# Input: [[0,30],[5,10],[15,20]]
# Output: false
# Example 2:
#
# Input: [[7,10],[2,4]]
# Output: true
