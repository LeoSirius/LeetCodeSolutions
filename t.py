from typing import *

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        _min = prices[0]
        _max = 0

        for price in prices:
            _min = min(_min, price)
            _max = max(_max, price - _min)

        return _max


def test(test_name, prices, expected):
    res = Solution().maxProfit(prices)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    prices1 = [7,1,5,3,6,4]
    expected1 = 5
    test('test1', prices1, expected1)

    prices2 = [7,6,4,3,1]
    expected2 = 0
    test('test2', prices2, expected2)

