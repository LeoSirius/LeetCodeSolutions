
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: Node = None, right: Node = None, next: Node = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        old_root = root
        first_before_level = Node()

        while root:
            p = first_before_level
            while root:
                if root.left:
                    p.next = root.left
                    p = p.next
                if root.right:
                    p.next = root.right
                    p = p.next
                root = root.next
            root = first_before_level.next
            first_before_level.next = None
        return old_root
