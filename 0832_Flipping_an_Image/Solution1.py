from typing import *


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        m, n = len(A), len(A[0])
        for i in range(m):
            for j in range(n):
                A[i][j] ^= 1
            A[i].reverse()

        return A


def test(test_name, A, expected):
    res = Solution().flipAndInvertImage(A)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    A1 = [
        [1,1,0],
        [1,0,1],
        [0,0,0]
    ]
    expected1 = [
        [1,0,0],
        [0,1,0],
        [1,1,1]
    ]
    test('test1', A1, expected1)

    A2 = [
        [1,1,0,0],
        [1,0,0,1],
        [0,1,1,1],
        [1,0,1,0]
    ]
    expected2 = [
        [1,1,0,0],
        [0,1,1,0],
        [0,0,0,1],
        [1,0,1,0]
    ]
    test('test2', A2, expected2)

