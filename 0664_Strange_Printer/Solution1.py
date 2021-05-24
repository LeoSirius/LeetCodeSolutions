class Solution:
    def strangePrinter(self, s: str) -> int:
        _len = len(s)
        dp = [[float('inf')] * _len for _ in range(_len)]

        for i in range(_len-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, _len):
                if s[i] == s[j]:
                    dp[i][j] = dp[i][j-1]
                else:
                    for k in range(i, j):
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j])

        return dp[0][_len-1]


def test(test_name, s, expected):
    res = Solution().strangePrinter(s)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    s1 = "aaabbb"
    expected1 = 2
    test('test1', s1, expected1)

    s2 = 'aba'
    expected2 = 2
    test('test2', s2, expected2)

    s3 = "abcabc"
    expected3 = 5
    test('test3', s3, expected3)
