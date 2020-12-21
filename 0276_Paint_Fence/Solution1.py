class Solution:
    def numWays(self, n: int, k: int) -> int:
        if not n or not k:
            return 0
        if n == 1:
            return k
        dp = [0 for i in range(n)]
        dp[0] = k
        dp[1] = k * k
        for i in range(2, n):
            dp[i] = (dp[i-1] + dp[i-2]) * (k-1)
        return dp[-1]

def test(test_name, n, k, expected):
    res = Solution().numWays(n, k)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    n1 = 3
    k1 = 2
    expected1 = 6
    test('test1', n1, k1, expected1)
