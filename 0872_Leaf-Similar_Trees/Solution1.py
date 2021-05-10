from util_py.tree import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:

        def preorder(node, leaf_array):
            if not node.left and not node.right:
                leaf_array.append(node.val)
            if node.left:
                preorder(node.left, leaf_array)
            if node.right:
                preorder(node.right, leaf_array)

        arr1, arr2 = [], []
        preorder(root1, arr1)
        preorder(root2, arr2)

        return arr1 == arr2


def test(test_name, root1, root2, expected):
    res = Solution().leafSimilar(root1, root2)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    #         3
    #       /   \
    #      5     1
    #    /  \   /  \
    #   6   2  9   8
    #      / \
    #     7  4
    root11 = TreeNode(3)
    root11.left = TreeNode(5)
    root11.left.left = TreeNode(6)
    root11.left.right = TreeNode(2)
    root11.left.right.left = TreeNode(7)
    root11.left.right.right = TreeNode(4)
    root11.right = TreeNode(1)
    root11.right.left = TreeNode(9)
    root11.right.right = TreeNode(8)
    #         3
    #       /   \
    #      5     1
    #    /  \   /  \
    #   6   7  4   2
    #             / \
    #            9  8
    root21 = TreeNode(3)
    root21.left = TreeNode(5)
    root21.left.left = TreeNode(6)
    root21.left.right = TreeNode(7)
    root21.right = TreeNode(1)
    root21.right.left = TreeNode(4)
    root21.right.right = TreeNode(2)
    root21.right.right.left = TreeNode(9)
    root21.right.right.right = TreeNode(8)
    expected1 = True
    test('test1', root11, root21, expected1)

    root12 = TreeNode(1)
    root22 = TreeNode(1)
    expected2 = True
    test('test2', root12, root22, expected2)

    root13 = TreeNode(1)
    root23 = TreeNode(2)
    expected3 = False
    test('test3', root13, root23, expected3)

    root14 = TreeNode(1)
    root14.left = TreeNode(2)
    root24 = TreeNode(2)
    root24.right = TreeNode(2)
    expected4 = True
    test('test4', root14, root24, expected4)

    root15 = TreeNode(1)
    root15.left = TreeNode(2)
    root15.right = TreeNode(3)

    root25 = TreeNode(1)
    root25.left = TreeNode(3)
    root25.right = TreeNode(2)
    expected5 = False
    test('test5', root15, root25, expected5)
