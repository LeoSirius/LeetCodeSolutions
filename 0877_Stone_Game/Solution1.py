from typing import *


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [[0] * (n+2) for _ in range(n+2)]

        # 枚举区间长度
        for _len in range(1, n+1):
            for l in range(1, n-_len+2):
                r = l+_len-1
                a = piles[l-1] - dp[l+1][r]
                b = piles[r-1] - dp[l][r-1]
                dp[l][r] = max(a, b)

        return bool(dp[1][n])


def test(test_name, piles, expected):
    res = Solution().stoneGame(piles)
    if type(res) == type(expected) and res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    piles1 = [5,3,4,5]
    expected1 = True
    test('test1', piles1, expected1)

