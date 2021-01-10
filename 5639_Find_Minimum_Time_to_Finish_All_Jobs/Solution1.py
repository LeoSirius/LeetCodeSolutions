from typing import *
import math

class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        jobs.sort()
        res = math.inf

        time = [0] * k  # time[i]表示第i个工人的时间

        def dfs(idx):
            nonlocal res, time, jobs, k
            
            # idx是完成工作的索引。这里表示所有工作都完成了
            if idx == len(jobs):
                t = max(time)
                res = min(t, res)
                return

            for i in range(k):
                if time[i] + jobs[idx] > res:  # i工人的时间已经超过了res，则不用看了
                    continue
                time[i] += jobs[idx]
                dfs(idx+1)
                time[i] -= jobs[idx]
                if time[i] == 0:
                    break
        dfs(0)
        return res



def test(test_name, jobs, k, expected):
    res = Solution().minimumTimeRequired(jobs, k)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    jobs1 = [3,2,3]
    k1 = 3
    expected1 = 3
    test('test1', jobs1, k1, expected1)

    jobs2 = [1,2,4,7,8]
    k2 = 2
    expected2 = 11
    test('test2', jobs2, k2, expected2)
