from typing import *

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        K = 2
        dp = [[0] * len(prices) for _ in range(K+1)]

        for k in range(1, K+1):
            cur_min = prices[0]
            for i in range(1, len(prices)):
                # 把思路中的j压缩到了cur_min，减少了一重循环
                cur_min = min(cur_min, prices[i]-dp[k-1][i-1])
                dp[k][i] = max(dp[k][i-1], prices[i]-cur_min)

        return dp[-1][-1]


def test(test_name, prices, expected):
    res = Solution().maxProfit(prices)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    prices1 = [3,3,5,0,0,3,1,4]
    expected1 = 6
    # test('test1', prices1, expected1)

    prices2 = [1,2,3,4,5]
    expected2 = 4
    test('test2', prices2, expected2)

    prices3 = [7,6,4,3,1]
    # expected3 = 0
    # test('test3', prices3, expected3)

    # prices4 = [1]
    # expected4 = 0
    # test('test4', prices4, expected4)


# Say you have an array for which the ith element is the price of 
# a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete at 
# most two transactions.

# Note: You may not engage in multiple transactions at the same time 
# (i.e., you must sell the stock before you buy again).


# Example 1:

# Input: prices = [3,3,5,0,0,3,1,4]
# Output: 6
# Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
# Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

# Example 2:

# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
# Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.

# Example 3:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.

# Example 4:

# Input: prices = [1]
# Output: 0
#  

# Constraints:

# 1 <= prices.length <= 105
# 0 <= prices[i] <= 105

