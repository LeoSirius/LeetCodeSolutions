from typing import *
from collections import defaultdict, Counter

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        root = [-1] * n

        sc = defaultdict(Counter)  # key是连通分量的跟（是索引），值是当前索引的值出现的次数
        tc = defaultdict(Counter)

        def find(x):
            if root[x] == -1:
                return x
            root[x] = find(root[x])
            return root[x]

        def join(a, b):
            A = find(a)
            B = find(b)
            if A != B:
                root[A] = B

        for a, b in allowedSwaps:
            join(a, b)

        for i in range(n):
            sc[find(i)][source[i]] += 1
            tc[find(i)][target[i]] += 1


        # 最后遍历每个连通分量的跟，
        res = 0
        for i in range(n):
            if root[i] == -1:
                # python中Counter相减，如果值是0，key会直接去掉
                res += sum((sc[i]-tc[i]).values())
        return res


def test(test_name, source, target, allowedSwaps, expected):
    res = Solution().minimumHammingDistance(source, target, allowedSwaps)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    source1 = [1,2,3,4]
    target1 = [2,1,4,5]
    allowedSwaps1 = [[0,1],[2,3]]
    expected1 = 1
    test('test1', source1, target1, allowedSwaps1, expected1)

    source2 = [1,2,3,4]
    target2 = [1,3,2,4]
    allowedSwaps2 = []
    expected2 = 2
    test('test2', source2, target2, allowedSwaps2, expected2)

    source3 = [5,1,2,4,3]
    target3 = [1,5,4,2,3]
    allowedSwaps3 = [[0,4],[4,2],[1,3],[1,4]]
    expected3 = 0
    test('test3', source3, target3, allowedSwaps3, expected3)

