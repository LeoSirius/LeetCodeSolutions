class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1 for _ in range(n)]
        p2, p3, p5 = 0, 0, 0

        for i in range(1, n):
            # 注意不要用elif，直接用if，不然如6，p2，p3都可以达到，就会重复
            dp[i] = min(dp[p2]*2, dp[p3]*3, dp[p5]*5)
            if dp[i] == dp[p2]*2:
                p2 += 1
            if dp[i] == dp[p3]*3:
                p3 += 1
            if dp[i] == dp[p5]*5:
                p5 += 1
        return dp[-1]


def test(test_name, n, expected):
    res = Solution().nthUglyNumber(n)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == "__main__":
    n1 = 10
    expected1 = 12
    test('test1', n1, expected1)