from typing import *
from math import sqrt


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        res = [area, 1]
        min_l = int(sqrt(area))
        for l in range(min_l, area + 1):
            if area % l != 0:
                continue
            w = area // l
            if l < w:
                continue
            res = [l, w]
            break
        return res


def test(test_name, area, expected):
    res = Solution().constructRectangle(area)
    if res == expected:
        print(test_name + ' succeed')
    else:
        print(test_name + ' fail')


if __name__ == '__main__':
    area1 = 4
    expected1 = [2,2]
    test('test1', area1, expected1)

    area2 = 37
    expected2 = [37, 1]
    test('test2', area2, expected2)

    area3 = 122122
    expected3 = [427,286]
    test('test3', area3, expected3)

    area4 = 2
    expected4 = [2,1]
    test('test4', area4, expected4)
