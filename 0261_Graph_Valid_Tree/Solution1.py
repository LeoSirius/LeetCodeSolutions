from typing import *
from collections import defaultdict

class Solution:

    def dfs(self, node):
        self.visited.add(node)
        for adj_node in self.graph[node]:
            if adj_node not in self.visited:
                self.dfs(adj_node)
                self.edges_cnt -= 1

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) >= n:
            return False

        self.graph = defaultdict(list)
        self.edges_cnt = len(edges)

        for x, y in edges:
            self.graph[x].append(y)
            self.graph[y].append(x)

        self.visited = set()

        self.dfs(0)

        # 第一个条件保证是连通图（所有结点都被访问过）
        return len(self.visited) == n


def test(test_name, n, edges, expected):
    res = Solution().validTree(n, edges)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    n1 = 5
    edges1 = [[0,1], [0,2], [0,3], [1,4]]
    expected1 = True
    test('test1', n1, edges1, expected1)

    n2 = 5
    edges2 = [[0,1], [1,2], [2,3], [1,3], [1,4]]
    expected2 = False
    test('test2', n2, edges2, expected2)

# Given n nodes labeled from 0 to n-1 and a list of undirected edges
#  (each edge is a pair of nodes), write a function to check whether 
#  these edges make up a valid tree.

# Example 1:

# Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
# Output: true

# Example 2:
# Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
# Output: false

# Note: you can assume that no duplicate edges will appear in edges.
#  Since all edges are undirected, [0,1] is the same as [1,0] and thus
#   will not appear together in edges.

