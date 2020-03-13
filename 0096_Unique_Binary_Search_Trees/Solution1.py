class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0 for i in range(n + 1)]
        dp[0] = dp[1] = 1

        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j-1] * dp[i-j]
        return dp[n]

def test(test_name, n, expected):
    res = Solution().numTrees(n)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    n1 = 3
    expected1 = 5
    test('test1', n1, expected1)
