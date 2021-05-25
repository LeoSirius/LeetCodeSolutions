from typing import *
from collections import defaultdict


class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        _max = 2 ** 10
        dp = [[float('inf')] * _max for _ in range(k)]
        g = [float('inf')] * k
        _len = len(nums)
        # print(f'len col = {len(dp[0])}')

        for i in range(k):
            cnt = 0                     # 统计每一列有多少个数字，最后一行的列不满
            counter = defaultdict(int)  # 统计每一列中每个数字的出现次数
            for j in range(i, _len, k):
                counter[nums[j]] += 1
                cnt += 1

            if i == 0:
                for xor in range(_max):
                    dp[0][xor] = min(dp[0][xor], cnt - counter.get(xor, 0))
                    g[0] = min(g[0], dp[0][xor])
            else:
                for xor in range(_max):
                    # 对整列进行修改替
                    res2 = g[i-1] + cnt

                    # 仅修改当列的部分数
                    res1 = float('inf')
                    for cur in counter:
                        res1 = min(res1, dp[i-1][xor ^ cur] + cnt - counter[cur])

                    dp[i][xor] = min(dp[i][xor], res1, res2)
                    g[i] = min(g[i], dp[i][xor])

        return dp[k-1][0]



def test(test_name, nums, k, expected):
    res = Solution().minChanges(nums, k)
    print(f'res = {res}')
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    nums1 = [1,2,0,3,0]
    k1 = 1
    expected1 = 3
    test('test1', nums1, k1, expected1)

    nums2 = [3,4,5,2,1,7,3,4,7]
    k2 = 3
    expected2 = 3
    test('test2', nums2, k2, expected2)

    nums3 = [1,2,4,1,2,5,1,2,6]
    k3 = 3
    expected3 = 3
    test('test3', nums3, k3, expected3)
