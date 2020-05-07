from typing import List

from utils_py.tree import *


class Solution:
    def dfs(self, node, path, res, sum):
        if not node:
            return
        remain = sum - node.val
        new_path = path[:]        # python这里必须copy一个新的对象，不然会污染上层
        new_path.append(node.val)
        if not node.left and not node.right:
            if remain == 0:
                res.append(new_path)
            return
        
        self.dfs(node.left, new_path, res, remain)
        self.dfs(node.right, new_path, res, remain)

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        self.dfs(root, [], res, sum)
        return res

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
    root1 = TreeNode(5);
    root1.left = TreeNode(4);
    root1.right = TreeNode(8);
    root1.left.left = TreeNode(11);
    root1.left.left.left = TreeNode(7);
    root1.left.left.right = TreeNode(2);
    root1.right.left = TreeNode(13);
    root1.right.right = TreeNode(4);
    root1.right.right.left = TreeNode(5);
    root1.right.right.right = TreeNode(1);
    sum1 = 22;
    expected1 = [
        [5,4,11,2], [5,8,4,5]
    ];
    test("test1", root1, sum1, expected1);
