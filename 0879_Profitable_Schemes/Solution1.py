from typing import *

class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10 ** 9 + 7

        _len = len(group)
        dp = [[[0] * (minProfit+1) for _ in range(n+1)] for _ in range(_len+1)]
        dp[0][0][0] = 1
        for i in range(1, _len+1):
            members, earn = group[i-1], profit[i-1]
            for j in range(n+1):
                for k in range(minProfit+1):
                    if j < members:
                        dp[i][j][k] = dp[i-1][j][k]
                    else:
                        dp[i][j][k] = (dp[i-1][j][k] + dp[i-1][j-members][max(0, k-earn)]) % MOD

        total = sum(dp[_len][j][minProfit] for j in range(n+1))
        return total % MOD


def test(test_name, n, minProfit, group, profit, expected):
    res = Solution().profitableSchemes(n, minProfit, group, profit)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    n1 = 5
    minProfit1 = 3
    group1 = [2,2]
    profit1 = [2,3]
    expected1 = 2
    test('test1', n1, minProfit1, group1, profit1, expected1)

    n2 = 10
    minProfit2 = 5
    group2 = [2,3,5]
    profit2 = [6,7,8]
    expected2 = 7
    test('test2', n2, minProfit2, group2, profit2, expected2)
