from typing import *

from utils_py.tree import *

class Solution:
    def dfs(self, path, node):
        path += [node.val]
        if (not node.left) and (not node.right):
            if sum(path) == self.sum:
                self.res.append(path[:])
        if node.left:
            self.dfs(path, node.left)
        if node.right:
            self.dfs(path, node.right)
        path.pop()

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []

        self.res = []
        self.root = root
        self.sum = sum
        self.dfs([], root)
        return self.res


def test(test_name, root, sum, expected):
    res = Solution().pathSum(root, sum)
    if sorted(res) == sorted(expected):
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == "__main__":
    #        5
    #       / \
    #      4   8
    #     /   / \
    #    11  13  4
    #   /  \    / \
    #  7    2  5   1
    root1 = TreeNode(5)
    root1.left = TreeNode(4)
    root1.right = TreeNode(8)
    root1.left.left = TreeNode(11)
    root1.left.left.left = TreeNode(7)
    root1.left.left.right = TreeNode(2)
    root1.right.left = TreeNode(13)
    root1.right.right = TreeNode(4)
    root1.right.right.left = TreeNode(5)
    root1.right.right.right = TreeNode(1)
    sum1 = 22
    expected1 = [
        [5,4,11,2], [5,8,4,5]
    ]
    # test("test1", root1, sum1, expected1)

    # 注意这个-2不是子节点，则不算path
    root2 = TreeNode(-2)
    root2.right = TreeNode(-3)
    sum2 = -2
    expected2 = []
    test('test2', root2, sum2, expected2)



# 输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。
# 从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。
