from util_py.tree import *


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        res = 0

        def preorder(node):
            nonlocal res
            if node.left:
                preorder(node.left)
            if low <= node.val <= high:
                res += node.val
            if node.right:
                preorder(node.right)
        preorder(root)

        return res


def test(test_name, root, low, high, expected):
    res = Solution().rangeSumBST(root, low, high)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    #         10
    #       /   \
    #      5    15
    #     / \    \
    #    3  7    18
    root1 = TreeNode(10)
    root1.left = TreeNode(5)
    root1.left.left = TreeNode(3)
    root1.left.right = TreeNode(7)
    root1.right = TreeNode(15)
    root1.right.right = TreeNode(18)
    low1 = 7
    high1 = 15
    expected1 = 32
    test('test1', root1, low1, high1, expected1)

    #         10
    #       /    \
    #      5     15
    #     / \   / \
    #    3   7 13 18
    #   /   /
    #  1   6
    root2 = TreeNode(10)
    root2.left = TreeNode(5)
    root2.left.left = TreeNode(3)
    root2.left.left.left = TreeNode(1)
    root2.left.right = TreeNode(7)
    root2.left.right.left = TreeNode(6)
    low2 = 6
    high2 = 10
    expected2 = 23
    test('test2', root2, low2, high2, expected2)
