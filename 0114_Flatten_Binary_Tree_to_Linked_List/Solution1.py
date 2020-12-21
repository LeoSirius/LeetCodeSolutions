from utils_py.tree import *

class Solution:
    last = None
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.flatten(root.right)
        self.flatten(root.left)
        root.right = self.last
        root.left = None
        self.last = root

def test(test_name, root, expected):
    Solution().flatten(root)
    if is_equal_tree(root, expected):
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    #      1
    #     / \
    #    2   5
    #   / \   \
    #  3   4   6
    root1 = TreeNode(1);
    root1 .left = TreeNode(2);
    root1 .left .left = TreeNode(3);
    root1 .left .right = TreeNode(4);
    root1 .right = TreeNode(5);
    root1 .right .right = TreeNode(6);

    #  1
    #   \
    #    2
    #     \
    #      3
    #       \
    #        4
    #         \
    #          5
    #           \
    #            6
    expected1 = TreeNode(1);
    expected1 .right = TreeNode(2);
    expected1 .right .right = TreeNode(3);
    expected1 .right .right .right = TreeNode(4);
    expected1 .right .right .right .right = TreeNode(5);
    expected1 .right .right .right .right .right = TreeNode(6);
    test("test1", root1, expected1);

