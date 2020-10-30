from utils_py.tree import *

class Solution:
    def is_sym(self, l: TreeNode, r: TreeNode):
        if not l and not r:
            return True
        if not l or not r:
            return False

        if l.val != r.val:
            return False
        return self.is_sym(l.right, r.left) and self.is_sym(l.left, r.right)

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.is_sym(root.left, root.right)

def test(test_name, root, expected):
    res = Solution().isSymmetric(root)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    #          1
    #         / \
    #        2   2
    #       / \ / \
    #      3  4 4  3
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(2)
    root1.left.left = TreeNode(3)
    root1.left.right = TreeNode(4)
    root1.right.left = TreeNode(4)
    root1.right.right = TreeNode(3)
    expected1 = True
    test('test1', root1, expected1)

    #          1
    #         / \
    #        2   2
    #       / \ / \
    #         3    3
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(2)
    root2.left.right = TreeNode(3)
    root2.right.right = TreeNode(3)
    expected2 = False
    test('test2', root2, expected2)

    root3 = None
    expected3 = True
    test('test3', root3, expected3)
