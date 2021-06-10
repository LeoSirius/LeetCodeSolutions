from typing import *


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for i in range(1, amount + 1):
            for coin in coins:
                if i < coin:
                    continue
                dp[i] += dp[i-coin]
        return dp[amount]


def test(test_name, amount, coins, expected):
    res = Solution().change(amount, coins)
    print(res)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    amount1 = 5
    coins1 = [1,2,5]
    expected1 = 4
    test('test1', amount1, coins1, expected1)

    amount2 = 3
    coins2 = [2]
    expected2 = 0
    test('test2', amount2, coins2, expected2)

    amount3 = 10
    coins3 = [10]
    expected3 = 1
    test('test3', amount3, coins3, expected3)

    amount4 = 500
    coins4 = [3,5,7,8,9,10,11]
    expected4 = 0
    test('test4', amount4, coins4, expected4)
