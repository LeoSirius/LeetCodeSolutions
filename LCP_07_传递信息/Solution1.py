from typing import *
from collections import defaultdict, deque


class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        persons = defaultdict(set)    # 每个人能到的 其他人处
        for rel in relation:
            persons[rel[0]].add(rel[1])

        que = deque([0])
        last_len = 1
        while que and k:
            while last_len:
                person = que.popleft()
                for end in persons[person]:
                    que.append(end)
                last_len -= 1
            k -= 1
            last_len = len(que)

        res = 0
        for end in que:
            if end == n-1:
                res += 1
        return res


def test(test_name, n, relation, k, expected):
    res = Solution().numWays(n, relation, k)
    if type(res) == type(expected) and res == expected:
        print(test_name + ' succeed')
    else:
        print(test_name + ' fail')


if __name__ == '__main__':
    n1 = 5
    relation1= [[0,2],[2,1],[3,4],[2,3],[1,4],[2,0],[0,4]]
    k1 = 3
    expected1 = 3
    test('test1', n1, relation1, k1, expected1)

    n2 = 3
    relation2 = [[0,2],[2,1]]
    k2 = 2
    expected2 = 0
    test('test2', n2, relation2, k2, expected2)
