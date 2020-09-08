from typing import *

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = list(range(n))  # 值如果等于自身，则是根，如果不是，则是父节点的索引

        def find(x):
            # 返回x所在连通区域的根结点
            if x == parents[x]:      # 自己就是跟节点
                return x
            return find(parents[x])  # 自己不是跟节点，则返回往父节点上继续追溯

        def union(x, y):
            # 把x和y合并到一个树里
            parents[find(x)] = parents[find(y)]

        # 把所有节点都合并 x,y是边的两个节点，必然是连通的
        for x, y in edges:
            union(x, y)

        # 最后查找有多少个根结点，去重再计数
        return len(set(map(find, range(n))))


def test(test_name, n, edges, expected):
    res = Solution().countComponents(n, edges)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    n1 = 5
    edges1 = [[0, 1], [1, 2], [3, 4]]
    #      0          3
    #      |          |
    #      1 --- 2    4 
    expected1 = 2
    test('test1', n1, edges1, expected1)

    n2 = 5
    edges2 = [[0, 1], [1, 2], [2, 3], [3, 4]]
    #      0           4
    #      |           |
    #      1 --- 2 --- 3
    expected2 = 1
    test('test2', n2, edges2, expected2)


# Given n nodes labeled from 0 to n - 1 and a list of undirected 
# edges (each edge is a pair of nodes), write a function to find the
#  number of connected components in an undirected graph.

# Example 1:

# Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

#      0          3
#      |          |
#      1 --- 2    4 

# Output: 2
# Example 2:

# Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

#      0           4
#      |           |
#      1 --- 2 --- 3

# Output:  1
# Note:
# You can assume that no duplicate edges will appear in edges. 
# Since all edges are undirected, [0, 1] is the same as [1, 0] and 
# thus will not appear together in edges.

