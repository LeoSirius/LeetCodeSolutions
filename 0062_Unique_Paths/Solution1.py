from typing import List

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1 for i in range(n)]
        # 注意这里是从1开始
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]
        return dp[n-1]

def test(test_name, m, n, expected):
    res = Solution().uniquePaths(m, n)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    m1, n1 = 3, 2
    expected1 = 3
    test('test1', m1, n1, expected1)

    m2, n2 = 7, 3
    expected2 = 28
    test('test2', m2, n2, expected2)
