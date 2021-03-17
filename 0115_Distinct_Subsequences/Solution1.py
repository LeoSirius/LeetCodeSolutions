class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0] * (len(t)+1) for _ in range(len(s)+1)]

        for i in range(len(s)+1):
            for j in range(len(t)+1):
                if j == 0:
                    dp[i][j] = 1
                elif i and j:
                    if s[i-1] == t[j-1]:
                        dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
                    else:
                        dp[i][j] = dp[i-1][j]

        return dp[-1][-1]


def test(test_name, s, t, expected):
    res = Solution().numDistinct(s, t)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    s1 = 'rabbbit'
    t1 = 'rabbit'
    expected1 = 3
    test('test1', s1, t1, expected1)

    s2 = 'babgbag'
    t2 = 'bag'
    expected2 = 5
    test('test2', s2, t2, expected2)

