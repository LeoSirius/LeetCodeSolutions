from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda l: l[0])
        res = intervals[:1]
        for pair in intervals[1:]:
            if res[-1][1] >= pair[0]:
                res[-1][1] = max(pair[1], res[-1][1])
            else:
                res.append(pair)
        return res



def test(test_name, intervals, expected):
    res = Solution().merge(intervals)
    print(res)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == "__main__":
    intervals1 = [[1,3],[2,6],[8,10],[15,18]]
    expected1 = [[1,6],[8,10],[15,18]]
    test("test1", intervals1, expected1)

    intervals2 = [[1,4],[4,5]]
    expected2 = [[1,5]]
    test("test2", intervals2, expected2)

    intervals3 = [[1,4],[0,4]]
    expected3 = [[0,4]]
    test('test3', intervals3, expected3)

    intervals4 = [[1,4],[2,3]]
    expected4 = [[1,4]]
    test('test4', intervals4, expected4)


# Given a collection of intervals, merge all overlapping intervals.

# Example 1:

# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:

# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
# NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

