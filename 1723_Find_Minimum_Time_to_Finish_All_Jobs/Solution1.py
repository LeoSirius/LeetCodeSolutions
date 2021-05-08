from typing import *
import math

class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        res = math.inf
        workers = [0] * k     # 每个工人分配的时间

        def dfs(n, max_of_worker):
            nonlocal res
            if n == len(jobs):
                res = min(res, max_of_worker)
                return

            for i in range(k):
                if workers[i] + jobs[n] >= res:
                    continue
                workers[i] += jobs[n]
                dfs(n+1, max(workers[i], max_of_worker))
                workers[i] -= jobs[n]
                # 必要的剪枝，不然会超时。若有工人没有分配，则其他工人的时间必然不是最小的
                if workers[i] == 0:
                    break

        # 遍历 i 个工人， 分配 n 份工作的所有情况
        dfs(0, 0)
        return res


def test(test_name, jobs, k, expected):
    res = Solution().minimumTimeRequired(jobs, k)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    jobs1 = [3,2,3]
    k1 = 3
    expected1 = 3
    test('test1', jobs1, k1, expected1)

    jobs2 = [1,2,4,7,8]
    k2 = 2
    expected2 = 11
    test('test2', jobs2, k2, expected2)
