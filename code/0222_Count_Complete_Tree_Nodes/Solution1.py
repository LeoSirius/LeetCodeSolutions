from util_py.tree import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        res = 0

        def preorder(node):
            nonlocal res
            if not node:
                return
            res += 1
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return res

def test(test_name, root, expected):
    res = Solution().countNodes(root)
    print(f'res = {res}')
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    root1.right = TreeNode(3)
    root1.right.left = TreeNode(6)
    expected1 = 6
    test('test1', root1, expected1)


# Given a complete binary tree, count the number of nodes.

# Note:

# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last, 
# is completely filled, and all nodes in the last level are as far left as possible. 
# It can have between 1 and 2h nodes inclusive at the last level h.

# Example:

# Input: 
#     1
#    / \
#   2   3
#  / \  /
# 4  5 6

# Output: 6
