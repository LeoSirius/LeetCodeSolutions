from utils_py.tree import *

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        stk = []
        

def test(test_name, root: TreeNode, k, expected):
    res = Solution().kthLargest(root, k)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == "__main__":
    root1 = TreeNode(3)
    root1.left = TreeNode(1)
    root1.right = TreeNode(4)
    root1.left.right = TreeNode(2)
    k1 = 1
    expected1 = 4
    test('test1', root1, k1, expected1)

# 输入: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# 输出: 4

# 给定一棵二叉搜索树，请找出其中第k大的节点。
# 1 ≤ k ≤ 二叉搜索树元素个数
