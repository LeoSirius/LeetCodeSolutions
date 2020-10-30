from typing import List
from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adjs = defaultdict(list)
        degrees = [0 for _ in range(n)]   # 索引就是node val，值是度
        for x, y in edges:
            adjs[x].append(y)
            adjs[y].append(x)
            degrees[x] += 1
            degrees[y] += 1

        layer = []
        # 先构建最外面一层
        for i, v in enumerate(degrees):
            if v == 1:
                layer.append(i)

        while layer:
            next_layer = []

            # 根据当前外层，获得下一层存到next_layer中
            for leaf in layer:
                for neighbor_of_leaf in adjs[leaf]:
                    degrees[neighbor_of_leaf] -= 1
                    if degrees[neighbor_of_leaf] == 1:
                        next_layer.append(neighbor_of_leaf)
            if not next_layer:  # 如果只剩一个或两个，则度是0，或-1，是加不到next_layer中的
                return layer
            layer = next_layer


def test(test_name, n, edges, expected):
    res = Solution().findMinHeightTrees(n, edges)
    if sorted(res) == sorted(expected):
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    n1 = 4
    edges1 = [[1, 0], [1, 2], [1, 3]]
    #         0
    #         |
    #         1
    #        / \
    #       2   3 
    expected1 = [1]
    test('test1', n1, edges1, expected1)

    n2 = 6
    edges2 = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
    #      0  1  2
    #       \ | /
    #         3
    #         |
    #         4
    #         |
    #         5 
    expected2 = [3, 4]
    test('test2', n2, edges2, expected2)



# For an undirected graph with tree characteristics, we can choose any node as the root.
#  The result graph is then a rooted tree. Among all possible rooted trees, those 
#  with minimum height are called minimum height trees (MHTs). Given such a graph,
#   write a function to find all the MHTs and return a list of their root labels.

# Format
# The graph contains n nodes which are labeled from 0 to n - 1. You will 
# be given the number n and a list of undirected edges (each edge is a pair of labels).

# You can assume that no duplicate edges will appear in edges. Since all 
# edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear 
# together in edges.

# Example 1 :
# Input: n = 4, edges = [[1, 0], [1, 2], [1, 3]]

#         0
#         |
#         1
#        / \
#       2   3 

# Output: [1]

# Example 2 :
# Input: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

#      0  1  2
#       \ | /
#         3
#         |
#         4
#         |
#         5 

# Output: [3, 4]

# Note:

# According to the definition of tree on Wikipedia: “
# a tree is an undirected graph in which any two vertices are connected 
# by exactly one path. In other words, any connected graph without simple
#  cycles is a tree.”
# The height of a rooted tree is the number of edges on the longest
#  downward path between the root and a leaf.

