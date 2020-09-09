from typing import *
from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(set)
        weight = defaultdict()     # 键是pair边，值是pair两个运算对应的value

        # 建图
        for i, v in enumerate(equations):
            graph[v[0]].add(v[1])
            graph[v[1]].add(v[0])

            # 边是有向的，因此权也有两个
            weight[tuple(v)] = values[i]
            weight[(v[1], v[0])] = float(1 / values[i])

        def dfs(start, end, visited):
            # 已求过两个节点的权重，则直接返回
            if (start, end) in weight:
                return weight[(start, end)]

            # 点不在图中 或 start 已经访问在前面的层中访问过
            if start not in graph or end not in graph:
                return 0
            if start in visited:
                return 0

            visited.add(start)
            res = 0
            for tmp in graph[start]:
                res = dfs(tmp, end, visited) * weight[(start, tmp)]
                if res != 0:
                    weight[(start, end)] = res
                    break
            visited.remove(start)
            return res


        res = []
        for start, end in queries:
            tmp = dfs(start, end, set())
            if tmp == 0:
                tmp = -1.0
            res.append(tmp)
        return res


def test(test_name, equations, values, queries, expected):
    res = Solution().calcEquation(equations, values, queries)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    equations1 = [["a", "b"], ["b", "c"]]
    values1 = [2.0, 3.0]
    queries1 = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    expected1 = [6.0, 0.5, -1.0, 1.0, -1.0 ]
    test('test1', equations1, values1, queries1, expected1)



# Equations are given in the format A / B = k, where A and B are variables 
# represented as strings, and k is a real number (floating point number). 
# Given some queries, return the answers. If the answer does not exist, return -1.0.

# Example:
# Given a / b = 2.0, b / c = 3.0.
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
# return [6.0, 0.5, -1.0, 1.0, -1.0 ].

# The input is: vector<pair<string, string>> equations, vector<double>& values,
#  vector<pair<string, string>> queries , where equations.size() == values.size(), 
#  and the values are positive. This represents the equations. Return vector<double>.

# According to the example above:

# equations = [ ["a", "b"], ["b", "c"] ],
# values = [2.0, 3.0],
# queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
#  

# The input is always valid. You may assume that evaluating the queries will
#  result in no division by zero and there is no contradiction.

