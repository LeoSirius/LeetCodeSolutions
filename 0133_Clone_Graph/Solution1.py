# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def __init__(self):
        self.visited = [None] * 101    # 建立val -> node的映射

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        new_node = Node(node.val)
        self.visited[new_node.val] = new_node

        for neighbor_node in node.neighbors:
            if not self.visited[neighbor_node.val]:
                new_node.neighbors.append(self.cloneGraph(neighbor_node))
            else:
                new_node.neighbors.append(self.visited[neighbor_node.val])

        return new_node

# 暂时不测