from utils_py.tree import *

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)

        # p.val <= root.val <= q.val
        return root


def test(test_name, root, p, q, expected):
    res = Solution().lowestCommonAncestor(root, p, q)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':

    #       6
    #     /   \
    #    2     8
    #   / \   / \
    #  0   4 7   9
    #     / \
    #    3   5
    root1 = TreeNode(6)
    root1.left = TreeNode(2)
    root1.left.left = TreeNode(0)
    root1.left.right = TreeNode(4)
    root1.left.right.left = TreeNode(3)
    root1.left.right.right = TreeNode(5)
    root1.right = TreeNode(8)
    root1.right.left = TreeNode(7)
    root1.right.right = TreeNode(9)
    # p1 = 6, q1 = 2, expected1 = 6
    p1 = root1
    q1 = root1.left
    expected1 = root1
    test('test1', root1, p1, q1, expected1)

    root2 = root1
    # p2 = 2, q2 = 4, expected2 = 2
    p2 = root2.left
    q2 = root2.left.right
    expected2 = p2
    test('test2', root2, p2, q2, expected2)


# 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

# 所有节点的值都是唯一的。
# p、q 为不同节点且均存在于给定的二叉搜索树中。
