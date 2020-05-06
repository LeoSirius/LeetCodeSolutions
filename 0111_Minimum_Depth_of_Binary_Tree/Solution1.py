from utils_py.tree import *

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        lnode, rnode = root.left, root.right
        if not lnode and not rnode:
            return 1
        l = self.minDepth(lnode)
        r = self.minDepth(rnode)
        if not lnode or not rnode:
            return l + r + 1
        return min(l, r) + 1


def test(test_name, root, expected):
    res = Solution().minDepth(root)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed')


if __name__ == "__main__":
    #     3
    #    / \
    #   9  20
    #     /  \
    #    15   7
    # return its minimum depth = 2.
    root1 = TreeNode(3);
    root1.left = TreeNode(9);
    root1.right = TreeNode(20);
    root1.right.left = TreeNode(15);
    root1.right.right = TreeNode(7);
    expected1 = 2;
    test("test1", root1, expected1);

    #    1
    #     \
    #     2
    root2 = TreeNode(1);
    root2.right = TreeNode(2);
    expected2 = 2;
    test("test2", root2, expected2);