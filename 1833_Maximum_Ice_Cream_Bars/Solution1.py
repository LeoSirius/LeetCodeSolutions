from typing import *


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        res = 0
        for cost in costs:
            coins -= cost
            if coins < 0:
                break
            res += 1
        return res


def test(test_name, costs, coins, expected):
    res = Solution().maxIceCream(costs, coins)
    if type(res) == type(expected) and res == expected:
        print(test_name + ' succeed')
    else:
        print(test_name + ' fail')


if __name__ == '__main__':
    costs1 = [1,3,2,4,1]
    coins1 = 7
    expected1 = 4
    test('test1', costs1, coins1, expected1)

    costs2 = [10,6,8,7,7,8]
    coins2 = 5
    expected2 = 0
    test('test2', costs2, coins2, expected2)

    costs3 = [1,6,3,1,2,5]
    coins3 = 20
    expected3 = 6
    test('test3', costs3, coins3, expected3)
