from typing import *


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        l, r = max(weights), sum(weights)

        def get_d_by_min_weight(min_w):
            d = 1
            cur_w = 0
            for w in weights:
                cur_w += w
                if cur_w > min_w:
                    d += 1
                    cur_w = w
            return d

        while l < r:
            m = l + (r - l) // 2
            d = get_d_by_min_weight(m)

            # 实际天数 > 目标天数：运力不足
            if d > D:
                l = m + 1
            else:
                r = m  # 否则说明运力剩余
        return l


def test(test_name, weights, D, expected):
    res = Solution().shipWithinDays(weights, D)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    weights1 = [1,2,3,4,5,6,7,8,9,10]
    D1 = 5
    expected1 = 15
    test('test1', weights1, D1, expected1)

    weights2 = [3,2,2,4,1,4]
    D2 = 3
    expected2 = 6
    test('test2', weights2, D2, expected2)

    weights3 = [1,2,3,1,1]
    D3 = 4
    expected3 = 3
    test('test3', weights3, D3, expected3)

    weights4 = [1,2,3,1,1]
    D4 = 4
    expected4 = 3
    test('test4', weights4, D4, expected4)
