from util_py.tree import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        root.left = self.mirrorTree(root.left)
        root.right = self.mirrorTree(root.right)
        root.left, root.right = root.right, root.left
        return root

def test(test_name, root, expected):
    res = Solution().mirrorTree(root)
    if is_equal_tree(res, expected):
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    #      4
    #    /   \
    #   2     7
    #  / \   / \
    # 1   3 6   9
    root1 = TreeNode(4)
    root1.left = TreeNode(2)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(3)
    root1.right = TreeNode(7)
    root1.right.left = TreeNode(6)
    root1.right.right = TreeNode(9)

    #      4
    #    /   \
    #   7     2
    #  / \   / \
    # 9   6 3   1
    expected1 = TreeNode(4)
    expected1.left = TreeNode(7)
    expected1.left.left = TreeNode(9)
    expected1.left.right = TreeNode(6)
    expected1.right = TreeNode(2)
    expected1.right.left = TreeNode(3)
    expected1.right.right = TreeNode(1)

    test("test1", root1, expected1)


# 请完成一个函数，输入一个二叉树，该函数输出它的镜像。

# 例如输入：

#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# 镜像输出：

#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1

# 限制：
# 0 <= 节点个数 <= 1000