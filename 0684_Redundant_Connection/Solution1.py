from typing import *

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parents = [i for i in range(0, n+1)]
        
        def find(x):
            if parents[x] == x: return x
            return find(parents[x])

        for edge in edges:
            a, b = find(edge[0]), find(edge[1])
            if a == b:
                return edge
            parents[a] = b


def test(test_name, edges, expected):
    res = Solution().findRedundantConnection(edges)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    #   1
    #  / \
    # 2 - 3
    edges1 = [[1,2], [1,3], [2,3]]
    expected1 = [2,3]
    test('test1', edges1, expected1)

    # 5 - 1 - 2
    #     |   |
    #     4 - 3
    edges2 = [[1,2], [2,3], [3,4], [1,4], [1,5]]
    expected2 = [1,4]
    test('test2', edges2, expected2)

# In this problem, a tree is an undirected graph that is connected and has no cycles.

# The given input is a graph that started as a tree with N nodes
#  (with distinct values 1, 2, ..., N), with one additional edge added. 
#  The added edge has two different vertices chosen from 1 to N,
#   and was not an edge that already existed.

# The resulting graph is given as a 2D-array of edges. Each element of edges is a pair
#  [u, v] with u < v, that represents an undirected edge connecting nodes u and v.

# Return an edge that can be removed so that the resulting graph is a tree of N nodes.
#  If there are multiple answers, return the answer that occurs last in the given
#   2D-array. The answer edge [u, v] should be in the same format, with u < v.

# Example 1:
# Input: [[1,2], [1,3], [2,3]]
# Output: [2,3]
# Explanation: The given undirected graph will be like this:
#   1
#  / \
# 2 - 3

# Example 2:
# Input: [[1,2], [2,3], [3,4], [1,4], [1,5]]
# Output: [1,4]
# Explanation: The given undirected graph will be like this:
# 5 - 1 - 2
#     |   |
#     4 - 3

# Note:
# The size of the input 2D-array will be between 3 and 1000.
# Every integer represented in the 2D-array will be between 1 and N, where N is 
# the size of the input array.
