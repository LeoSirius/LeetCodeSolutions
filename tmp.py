class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0 for i in range(len(s) + 1)]
        dp[0] = 1
        for i in range(1, len(s) + 1):
            if 1 <= int(s[i-1]) <= 9:
                dp[i] = dp[i-1]
            if i > 1 and 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        return dp[-1]


def test(test_name, s, expected):
    res = Solution().numDecodings(s)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == "__main__":
    s1 = "12"
    expected1 = 2
    test('test1', s1, expected1)

    s2 = "226"
    expected2 = 3
    test('test2', s2, expected2)

    s3 = "0"
    expected3 = 0
    test('test3', s3, expected3)

    s4 = "01"
    expected4 = 0
    test('test4', s4, expected4)