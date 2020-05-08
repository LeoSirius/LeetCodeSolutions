from utils_py.tree import *

class Solution:
    def is_sym(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val == q.val:
            return self.is_sym(p.left, q.right) and self.is_sym(p.right, q.left)
        return False

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
    t1 = TreeNode(1);
    t1.left = TreeNode(2);
    t1.right = TreeNode(2);
    t1.left.left = TreeNode(3);
    t1.left.right = TreeNode(4);
    t1.right.left = TreeNode(4);
    t1.right.right = TreeNode(3);
    expected1 = True;
    #     1
    #    / \
    #   2   2
    #  / \ / \
    # 3  4 4  3
    test("test1", t1, expected1);

    t2 = TreeNode(1);
    t2.left = TreeNode(2);
    t2.left.right = TreeNode(3);
    t2.right = TreeNode(2);
    t2.right.right = TreeNode(3);
    expected2 = False;
    #     1
    #    / \
    #   2   2
    #    \   \
    #    3    3
    test("test2", t2, expected2);

    t3 = None;
    expected3 = True;
    test("test3", t3, expected3);
