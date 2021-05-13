class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9+7
        _max = min(steps // 2, arrLen - 1)
        dp = [[0] * (_max+1) for _ in range(steps+1)]
        dp[0][0] = 1

        for i in range(1, steps+1):
            for j in range(_max+1):
                dp[i][j] += dp[i-1][j]
                if j - 1 >= 0:
                    dp[i][j] += dp[i-1][j-1]
                if j + 1 <= _max:
                    dp[i][j] += dp[i-1][j+1]

        return dp[steps][0] % MOD


def test(test_name, steps, arrLen, expected):
    res = Solution().numWays(steps, arrLen)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    steps1 = 3
    arrLen1 = 2
    expected1 = 4
    test('test1', steps1, arrLen1, expected1)

    steps2 = 2
    arrLen2 = 4
    expected2 = 2
    test('test2', steps2, arrLen2, expected2)

    steps3 = 4
    arrLen3 = 2
    expected3 = 8
    test('test3', steps3, arrLen3, expected3)
