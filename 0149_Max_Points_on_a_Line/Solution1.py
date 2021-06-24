from typing import *


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        _len = len(points)

        def is_in_line(a, b, c):
            dx1 = b[0] - a[0]
            dy1 = b[1] - a[1]
            dx2 = b[0] - c[0]
            dy2 = b[1] - c[1]
            return dy1 * dx2 == dy2 * dx1

        res = 1
        for i in range(_len):
            for j in range(i+1, _len):
                cnt = 2
                for p in points:
                    if p == points[i] or p == points[j]:
                        continue
                    if is_in_line(points[i], points[j], p):
                        cnt += 1
                res = max(res, cnt)
        return res


def test(test_name, points, expected):
    res = Solution().maxPoints(points)
    if type(res) == type(expected) and res == expected:
        print(test_name + ' succeed')
    else:
        print(test_name + ' fail')


if __name__ == '__main__':
    points1 = [[1,1],[2,2],[3,3]]
    expected1 = 3
    test('test1', points1, expected1)

    points2 = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    expected2 = 4
    test('test2', points2, expected2)

    points3 = [[0,0]]
    expected3 = 1
    test('test3', points3, expected3)
