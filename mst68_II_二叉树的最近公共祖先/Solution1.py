from utils_py.tree import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == p or root == q:
            return root
        
        left_sub_node = self.lowestCommonAncestor(root.left, p, q)
        right_sub_node = self.lowestCommonAncestor(root.right, p, q)

        # p q 同时在root.left和root.right的下面，则必然是在两边，返回root
        # right_sub是空，说明pq同时在left_sub_node及其下面，且left_sub_node是那个最高的节点
        if left_sub_node and right_sub_node:
            return root
        elif left_sub_node:
            return left_sub_node
        else:
            return right_sub_node


def test(test_name, root, p, q, expected):
    res = Solution().lowestCommonAncestor(root, p, q)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    #       3
    #     /   \
    #    5     1
    #   / \   / \
    #  6   2 0   8
    #     / \
    #    7   4
    root1 = TreeNode(3)
    root1.left = TreeNode(5)
    root1.left.left = TreeNode(6)
    root1.left.right = TreeNode(2)
    root1.left.right.left = TreeNode(7)
    root1.left.right.right = TreeNode(4)

    root1.right = TreeNode(1)
    root1.right.left = TreeNode(0)
    root1.right.right = TreeNode(8)

    p1 = root1.left
    q1 = root1.right

    expected1 = root1
    # p1 = 5, q1 = 1, expected1 = 3
    test("test1", root1, p1, q1, expected1)

    root2 = root1
    p2 = root2.left
    q2 = root2.left.right.right
    expected2 = root2.left
    # p2 = 5, q2 = 4, expected2 = 5
    test("test2", root2, p2, q2, expected2)


#  给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

#  百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，
#  满足 x 是 p、q 的祖先且 x 的深度尽可能大（x本身尽可能的深）（一个节点也可以是它自己的祖先）。”
