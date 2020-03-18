import sys

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [sys.maxsize for i in range(n+1)]
        dp[0] = 0

        for i in range(1, n+1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i-j*j] + 1)
                j += 1
        return dp[-1]


def test(test_name, n, expected):
    res = Solution().numSquares(n)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    n1 = 12
    expected1 = 3
    test('test1', n1, expected1)

    n2 = 13
    expected2 = 2
    test('test2', n2, expected2)
