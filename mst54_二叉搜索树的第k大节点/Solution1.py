from utils_py.tree import *

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        stk = []
        p = root
        while p or stk:
            while p:
                stk.append(p)
                p = p.right
            p = stk.pop()
            k -= 1
            if k == 0:
                return p.val
            p = p.left

def test(test_name, root, k, expected):
    res = Solution().kthLargest(root, k)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    root1 = TreeNode(3)
    root1.left = TreeNode(1)
    root1.left.right = TreeNode(2)
    root1.right = TreeNode(4)
    #    3
    #   / \
    #  1   4
    #   \
    #    2
    k1 = 1
    expected1 = 4
    test('test1', root1, k1, expected1)

    root2 = TreeNode(5)
    root2.left = TreeNode(3)
    root2.left.left = TreeNode(2)
    root2.left.right = TreeNode(4)
    root2.left.left.left = TreeNode(1)
    root2.right = TreeNode(6)
    #        5
    #       / \
    #      3   6
    #     / \
    #    2   4
    #   /
    #  1
    k2 = 3
    expected2 = 4
    test('test2', root2, k2, expected2)


# 给定一棵二叉搜索树，请找出其中第k大的节点。

# 限制：
# 1 ≤ k ≤ 二叉搜索树元素个数
