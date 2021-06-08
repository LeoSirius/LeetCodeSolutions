from typing import *


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        _sum = sum(stones)
        target_weight = _sum // 2
        # dp[i] 表示：是否有子集数组，重量和为i，值为 True or False
        dp = [False] * (target_weight + 1)
        dp[0]= True

        for stone in stones:
            for i in range(target_weight, stone-1, -1):
                dp[i] = dp[i] or dp[i-stone]

        for i in range(target_weight, -1, -1):
            if dp[i]:
                return _sum - 2 * i


def test(test_name, stones, expected):
    res = Solution().lastStoneWeightII(stones)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    stones1 = [2,7,4,1,8,1]
    expected1 = 1
    test('test1', stones1, expected1)

    stones2 = [31,26,33,21,40]
    expected2 = 5
    test('test2', stones2, expected2)

    stone3 = [1,2]
    expected3 = 1
    test('test3', stone3, expected3)
