from utils_py.tree import *

class Solution:

    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        stk = []
        p = root
        last_val = None
        while p or stk:
            while p:
                stk.append(p)
                p = p.left
            p = stk.pop()
            if last_val != None and last_val >= p.val:
                return False
            last_val = p.val
            p = p.right
        return True

def test(test_name, root, expected):
    res = Solution().isValidBST(root)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == "__main__":
    tree1 = TreeNode(2);
    tree1.left = TreeNode(1);
    tree1.right = TreeNode(3);
    expected1 = True;
    #     2
    #    / \
    #   1   3
    # Output: true
    test("test1", tree1, expected1);

    tree2 = TreeNode(5);
    tree2.left = TreeNode(1);
    tree2.right = TreeNode(4);
    tree2.right.left = TreeNode(3);
    tree2.right.right = TreeNode(6);
    expected2 = False;
    #     5
    #    / \
    #   1   4
    #      / \
    #     3   6
    # Output: false
    test("test2", tree2, expected2);

    tree3 = TreeNode(10);
    tree3.left = TreeNode(5);
    tree3.right = TreeNode(15);
    tree3.right.left = TreeNode(6);
    tree3.right.right = TreeNode(20);
    expected3 = False;
    #    10
    #   /  \
    #  5   15
    #     /  \
    #    6    20
    #   false
    test("test3", tree3, expected3);

    tree4 = TreeNode(1);
    tree4.left = TreeNode(1);
    expected4 = False;
    test("test4", tree4, expected4);

    tree5 = TreeNode(0)
    tree5.right = TreeNode(-1)
    expected5 = False
    test("test5", tree5, expected5)
