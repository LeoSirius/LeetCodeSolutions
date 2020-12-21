from typing import *

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def dfs(start, path):
            if len(path) == k:
                res.append(path)
                return
            
            for i in range(start + 1, n + 1):
                dfs(i, path + [i])   # 这里和排列的不同之处，start传的是i
        
        dfs(0, [])
        return res



def test(test_name, n, k, expected):
    res = Solution().combine(n, k)
    res.sort()
    expected.sort()
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    n1, k1 = 4, 2
    expected1 = [
        [2,4,], [3,4], [2,3], [1,2], [1,3], [1,4]
    ];
    test("test1", n1, k1, expected1);


# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

# 示例:

# 输入: n = 4, k = 2
# 输出:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
