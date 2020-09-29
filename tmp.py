from utils_py.tree import *

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root.val == p.val or root.val == q.val:
            return root

        find_one_in_left = self.lowestCommonAncestor(root.left, p, q)
        find_one_in_right = self.lowestCommonAncestor(root.right, p, q)

        if find_one_in_left and find_one_in_right:
            return root
        elif find_one_in_left:
            return find_one_in_left
        else:
            return find_one_in_right


def test(test_name, root, p, q, expected):
    res = Solution().lowestCommonAncestor(root, p, q)
    if res.val == expected.val:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    #      3
    #    /   \
    #   5     1
    #  / \   / \
    # 6   2 0   8
    #    / \
    #   7   4
    root1 = TreeNode(3)
    root1.left = TreeNode(5)
    root1.left.left = TreeNode(6)
    root1.left.right = TreeNode(2)
    root1.left.right.left = TreeNode(7)
    root1.left.right.right = TreeNode(4)
    root1.right = TreeNode(1)
    root1.right.left = TreeNode(0)
    root1.right.right = TreeNode(8)
    # p1 = 5, q1 = 1, expected1 = 3
    p1 = root1.left
    q1 = root1.right
    expected1 = root1
    test('test1', root1, p1, q1, expected1)

    root2 = root1
    # p2 = 5, q2 = 4, expected2 = 5
    p2 = root2.left
    q2 = p2.right.right
    expected2 = p2
    test('test2', root2, p2, q2, expected2)


# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，
# 满足 x 是 p、q 的祖先且 x 的深度尽可能大（x本身尽可能的深）（一个节点也可以是它自己的祖先）。”

# 所有节点的值都是唯一的。
# p、q 为不同节点且均存在于给定的二叉树中。