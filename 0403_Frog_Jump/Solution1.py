from typing import *


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        next_idx2stone_idx = {}
        for i, v in enumerate(stones):
            next_idx2stone_idx[v] = i
        cache = {}

        def dfs(idx, k):
            cache_key = str(idx) + str(k)
            if cache_key in cache:
                return cache[cache_key]

            if idx == len(stones) - 1:
                return True

            for i in [-1, 0, 1]:
                if k + i == 0:   # 原地跳步，跳过
                    continue
                next_idx = stones[idx] + k + i
                if next_idx in next_idx2stone_idx:
                    res = dfs(next_idx2stone_idx[next_idx], k + i)
                    if res:
                        cache[cache_key] = True
                        return True
            cache[cache_key] = False
            return False
        
        if 1 not in next_idx2stone_idx:
            return False
        return dfs(1, 1)


def test(test_name, stones, expected):
    res = Solution().canCross(stones)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    stones1 = [0,1,3,5,6,8,12,17]
    expected1 = True
    test('test1', stones1, expected1)

    stones2 = [0,1,2,3,4,8,9,11]
    expected2 = False
    test('test2', stones2, expected2)
