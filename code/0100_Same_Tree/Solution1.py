from utils_py.tree import *

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

def test(test_name, p, q, expected):
    res = Solution().isSameTree(p, q)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    p1 = TreeNode(1)
    p1.left = TreeNode(2)
    p1.right = TreeNode(3)

    q1 = TreeNode(1)
    q1.left = TreeNode(2)
    q1.right = TreeNode(3)

    expected1 = True
    test('test1', p1, q1, expected1)

    p2 = TreeNode(0)
    p2.right = TreeNode(-5)

    q2 = TreeNode(0)
    q2.right = TreeNode(-1)

    expected2 = False
    test('test2', p2, q2, expected2)
