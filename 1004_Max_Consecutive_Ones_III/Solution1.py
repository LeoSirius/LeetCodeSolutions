from typing import *


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        res = 0
        l, r = 0, 0
        zeros = 0

        while r < len(A):
            if A[r] == 0:
                zeros += 1
            while zeros > K:
                if A[l] == 0:
                    zeros -= 1
                l += 1
            res = max(res, r + 1 - l)
            r += 1

        return res


def test(test_name, A, K, expected):
    res = Solution().longestOnes(A, K)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    A1 = [1,1,1,0,0,0,1,1,1,1,0]
    K1 = 2
    expected1 = 6
    test('test1', A1, K1, expected1)

    A2 = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    K2 = 3
    expected2 = 10
    test('test2', A2, K2, expected2)

