from utils_py.tree import *

class Solution:

    def get_depth(self, root):
        if not root:
            return 0
        return max(self.get_depth(root.left), self.get_depth(root.right)) + 1
    def maxDepth(self, root: TreeNode) -> int:
        return self.get_depth(root)


def test(test_name, root, expected):
    res = Solution().maxDepth(root)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    t1 = TreeNode(3);
    t1.left = TreeNode(9);
    t1.right = TreeNode(20);
    t1.right.left = TreeNode(15);
    t1.right.right = TreeNode(7);
    expected1 = 3;
    #      3
    #     / \
    #    9  20
    #      /  \
    #     15   7
    test("test1", t1, expected1);
