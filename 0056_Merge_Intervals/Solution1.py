from typing import List

class Solution:
    def compare_first(self, item):
        return item[0]
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        if not intervals:
            return res
        intervals.sort(key=self.compare_first)

        res.append(intervals[0])
        for i in range(1, len(intervals)):
            if res[-1][1] < intervals[i][0]:
                res.append(intervals[i])
            else:
                res[-1][1] = max(res[-1][1], intervals[i][1])
        return res


def test(test_name, intervals, expected):
    res = Solution().merge(intervals)
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
