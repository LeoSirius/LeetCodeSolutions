
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.head, self.pre = None, None

    def dfs(self, node):
        if not node:
            return

        self.dfs(node.left)

        if not self.head:
            self.head, self.pre = node, node
        else:
            self.pre.right, node.left = node, self.pre
            self.pre = node

        self.dfs(node.right)

    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        self.dfs(root)
        self.head.left, self.pre.right = self.pre, self.head
        return self.head


def is_equal(head1, head2):

    if not head1 and not head2:
        return True
    if not head1 or not head2:
        return False

    if head1.val != head2.val:
        return False
    p1, p2 = head1.right, head2.right
    while p1 != head1 and p2 != head2:
        if p1.val != p2.val:
            return False
        p1, p2 = p1.right, p2.right
    return True

def test(test_name, root, expected):
    # 这道题遍历一遍双向链表，判断是不是所有结点的值都相同
    res = Solution().treeToDoublyList(root)
    if is_equal(res, expected):
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    #     4
    #    / \
    #   2   5
    #  / \
    # 1   3
    root1 = Node(4)
    root1.left = Node(2)
    root1.left.left = Node(1)
    root1.left.right = Node(3)
    root1.right = Node(5)
    # 1 -> 2 -> 3 -> 4 -> 5
    expected1 = Node(1)
    expected1.right = Node(2)
    expected1.right.right = Node(3)
    expected1.right.right.right = Node(4)
    expected1.right.right.right.right = Node(5)
    expected1.right.right.right.right.right = expected1
    expected1.left = expected1.right.right.right.right.right
    expected1.right.left = expected1
    expected1.right.right.left = expected1.right
    expected1.right.right.right.left = expected1.right.right
    expected1.right.right.right.right.left = expected1.right.right.right
    expected1.right.right.right.right.right.left = expected1.right.right.right.right

    test("test1", root1, expected1)

    root2 = None
    expected2 = None
    test('test2', root2, expected2)


# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。
# 要求不能创建任何新的节点，只能调整树中节点指针的指向。
