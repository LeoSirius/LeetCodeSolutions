from typing import List

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        dp = [0 for i in range(n)]
        dp[0], dp[1] = 1, 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1]

def test(test_name, n, expected):
    res = Solution().climbStairs(n)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == "__main__":
    n1 = 2
    expected1 = 2
    test('test1', n1, expected1)

    n2 = 3
    expected2 = 3
    test('test2', n2, expected2)

    n3 = 1
    expected3 = 1
    test('test3', n3, expected3)
