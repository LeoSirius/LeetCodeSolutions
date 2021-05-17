from util_py.tree import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def get_parent_with_dep(node, x, dep):
            res = (None, None)
            if node.left:
                if node.left.val == x:
                    res = node.val, dep+1
                else:
                    res = get_parent_with_dep(node.left, x, dep+1)

            if res != (None, None):
                return res

            if node.right:
                if node.right.val == x:
                    res = node.val, dep+1
                else:
                    res = get_parent_with_dep(node.right, x, dep+1)
            return res

        px, dx = get_parent_with_dep(root, x, 1)
        py, dy = get_parent_with_dep(root, y, 1)
        return px != py and dx == dy


def test(test_name, root, x, y, expected):
    res = Solution().isCousins(root, x, y)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    #         1
    #        / \
    #       2   3
    #      /
    #     4
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.left.left = TreeNode(4)
    root1.right = TreeNode(3)
    x1, y1 = 4, 3
    expected1 = False
    test('test1', root1, x1, y1, expected1)

    #         1
    #        / \
    #       2   3
    #        \   \
    #        4    5
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.left.right = TreeNode(4)
    root2.right = TreeNode(3)
    root2.right.right = TreeNode(5)
    x2, y2 = 5, 4
    expected2 = True
    test('test2', root2, x2, y2, expected2)

    #         1
    #        / \
    #       2   3
    #        \
    #        4
    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    root3.left.right = TreeNode(4)
    root3.right = TreeNode(3)
    x3, y3 = 2, 3
    expected3 = False
    test('test3', root3, x3, y3, expected3)

    #        1
    #         \
    #          2
    #         /
    #        3
    #         \
    #         4
    #          \
    #          5
    root4 = TreeNode(1)
    root4.right = TreeNode(2)
    root4.right.left = TreeNode(3)
    root4.right.left.right = TreeNode(4)
    root4.right.left.right.right = TreeNode(5)
    x4, y4 = 1, 3
    expected4 = False
    test('test4', root4, x4, y4, expected4)
