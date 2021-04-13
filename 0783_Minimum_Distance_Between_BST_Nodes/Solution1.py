from util_py.tree import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        diff = float('inf')
        stk = []
        prev = None

        while stk or root:
            while root:
                stk.append(root)
                root = root.left
            root = stk.pop()
            if prev:
                diff = min(diff, abs(prev.val - root.val))
            prev = root
            root = root.right

        return diff


def test(test_name, root, expected):
    res = Solution().minDiffInBST(root)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    #      4
    #    /  \
    #   2   6
    #  / \
    # 1  3
    root1 = TreeNode(4)
    root1.left = TreeNode(2)
    root1.right = TreeNode(6)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(3)
    expected1 = 1
    test('test1', root1, expected1)

    #      1
    #    /  \
    #   0   48
    #      /  \
    #     12   49
    root2 = TreeNode(1)
    root2.left = TreeNode(0)
    root2.right = TreeNode(48)
    root2.right.left = TreeNode(12)
    root2.right.right = TreeNode(49)
    expected2 = 1
    test('test2', root2, expected2)

    #       90
    #      /
    #     69
    #    /  \
    #   49  89
    #    \
    #    52
    root3 = TreeNode(90)
    root3.left = TreeNode(69)
    root3.left.left = TreeNode(49)
    root3.left.right = TreeNode(89)
    root3.left.left.right = TreeNode(52)
    expected3 = 1
    test('test3', root3, expected3)
