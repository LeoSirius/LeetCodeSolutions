from typing import *


class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        res = []
        presum = [0] * (len(candiesCount)+1)
        for i in range(1, len(candiesCount)+1):
            presum[i] = presum[i-1] + candiesCount[i-1]

        for query in queries:
            t, d, c = query[0], query[1] + 1, query[2]
            l = presum[t] // c + 1
            r = presum[t+1]
            res.append(l <= d <= r)

        return res


def test(test_name, candiesCount, queries, expected):
    res = Solution().canEat(candiesCount, queries)
    print(f'res = {res}')
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    candiesCount1 = [7,4,5,3,8]
    queries1 = [[0,2,2],[4,2,4],[2,13,1000000000]]
    expected1 = [True, False, True]
    test('test1', candiesCount1, queries1, expected1)

    candiesCount2 = [5,2,6,4,1]
    queries2 = [[3,1,2],[4,10,3],[3,10,100],[4,100,30],[1,3,1]]
    expected2 = [False,True,True,False,False]
    test('test2', candiesCount2, queries2, expected2)
