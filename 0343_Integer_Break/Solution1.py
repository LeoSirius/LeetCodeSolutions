class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [1] * (n + 1)
        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], j * (i-j), j * dp[i-j])

        return dp[-1]


def test(test_name, n, expected):
    res = Solution().integerBreak(n)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    n1 = 2
    expected1 = 1
    test('test1', n1, expected1)

    n2 = 10
    expected2 = 36
    test('test2', n2, expected2)

