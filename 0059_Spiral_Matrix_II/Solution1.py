from typing import *


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        left, right, top, bottom = 0, n-1, 0, n-1

        k = 1
        while left <= right and top <= bottom:
            for i in range(left, right+1):
                res[top][i] = k
                k += 1
            top += 1
            for j in range(top, bottom+1):
                res[j][right] = k
                k += 1
            right -= 1
            if left > right or top > bottom:
                break
            for i in range(right, left-1, -1):
                res[bottom][i] = k
                k += 1
            bottom -= 1
            for j in range(bottom, top-1, -1):
                res[j][left] = k
                k += 1
            left += 1
        return res


def test(test_name, n, expected):
    res = Solution().generateMatrix(n)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    n1 = 3
    expected1 = [
        [ 1, 2, 3 ],
        [ 8, 9, 4 ],
        [ 7, 6, 5 ]
    ]
    test('test1', n1, expected1)


