from typing import *

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # edges中节点的编号是从1开始的，留出0索引不管，方便处理
        parents_ali = [-1] * (n + 1)
        parents_bob = [-1] * (n + 1)

        def find(x, parents):
            if parents[x] == -1:
                return x
            root = find(parents[x], parents)
            parents[x] = root
            return root

        def merge(a, b, parents):
            A, B = find(a, parents), find(b, parents)
            if A != B:
                parents[A] = B

        res = 0

        for _type, n1, n2 in edges:
            if _type == 3:
                # 类型3，两人都能连通。ali能连通，则bob也能连通
                root1 = find(n1, parents_ali)
                root2 = find(n2, parents_ali)
                if root1 == root2 and root1 != -1:
                    # 如果他们已经可以连通了，说明这条类型3的边是多余的
                    res += 1
                else:
                    # 如果这两点不能连通，则把类型3的边转换成他们两人的边
                    merge(n1, n2, parents_ali)
                    merge(n1, n2, parents_bob)

        for _type, n1, n2 in edges:
            if _type == 1:
                root1 = find(n1, parents_ali)
                root2 = find(n2, parents_ali)
                if root1 == root2 and root1 != -1:
                    res += 1
                else:
                    merge(n1, n2, parents_ali)
            elif _type == 2:
                root1 = find(n1, parents_bob)
                root2 = find(n2, parents_bob)
                if root1 == root2 and root1 != -1:
                    res += 1
                else:
                    merge(n1, n2, parents_bob)

        num_of_root_ali, num_of_root_bob = 0, 0
        for i in range(1, n+1):
            if parents_ali[i] == -1:
                num_of_root_ali += 1
        for i in range(1, n+1):
            if parents_bob[i] == -1:
                num_of_root_bob += 1
        if num_of_root_ali * num_of_root_bob > 1:
            return -1

        return res


def test(test_name, n, edges, expected):
    res = Solution().maxNumEdgesToRemove(n, edges)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    n1 = 4
    edges1 = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
    expected1 = 2
    test('test1', n1, edges1, expected1)

    n2 = 4
    edges2 = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
    expected2 = 0
    test('test2', n2, edges2, expected2)

    n3 = 4
    edges3 = [[3,2,3],[1,1,2],[2,3,4]]
    expected3 = -1
    test('test3', n3, edges3, expected3)


# Alice and Bob have an undirected graph of n nodes and 3
#  types of edges:

# Type 1: Can be traversed by Alice only.
# Type 2: Can be traversed by Bob only.
# Type 3: Can by traversed by both Alice and Bob.
# Given an array edges where edges[i] = [typei, ui, vi] 
# represents a bidirectional edge of type typei between 
# nodes ui and vi, find the maximum number of edges you can 
# remove so that after removing the edges, the graph can still 
# be fully traversed by both Alice and Bob. The graph is fully
#  traversed by Alice and Bob if starting from any node, they 
#  can reach all other nodes.

# Return the maximum number of edges you can remove, or return -1 
# if it's impossible for the graph to be fully traversed by Alice 
# and Bob.


# Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
# Output: 2
# Explanation: If we remove the 2 edges [1,1,2] and [1,1,3]. 
# The graph will still be fully traversable by Alice and Bob. 
# Removing any additional edge will not make it so. So the 
# maximum number of edges we can remove is 2.


# Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
# Output: 0
# Explanation: Notice that removing any edge will not make 
# the graph fully traversable by Alice and Bob.


# Input: n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
# Output: -1
# Explanation: In the current graph, Alice cannot reach node 
# 4 from the other nodes. Likewise, Bob cannot reach 1. 
# Therefore it's impossible to make the graph fully traversable.


# Constraints:

# 1 <= n <= 10^5
# 1 <= edges.length <= min(10^5, 3 * n * (n-1) / 2)
# edges[i].length == 3
# 1 <= edges[i][0] <= 3
# 1 <= edges[i][1] < edges[i][2] <= n
# All tuples (typei, ui, vi) are distinct.

