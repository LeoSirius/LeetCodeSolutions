from utils_py.tree import *

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return sum == root.val
        
        remain = sum - root.val
        return self.hasPathSum(root.left, remain) or self.hasPathSum(root.right, remain)


def test(test_name, root, sum, expected):
    res = Solution().hasPathSum(root, sum)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == "__main__":
    #        5
    #       / \
    #      4   8
    #     /   / \
    #    11  13  4
    #   /  \      \
    #  7    2      1
    root1 = TreeNode(5);
    root1.left = TreeNode(4);
    root1.right = TreeNode(8);
    root1.left.left = TreeNode(11);
    root1.left.left.left = TreeNode(7);
    root1.left.left.right = TreeNode(2);
    root1.right.left = TreeNode(13);
    root1.right.right = TreeNode(4);
    root1.right.right.right = TreeNode(1);
    sum1 = 22;
    expected1 = True;
    test("test1", root1, sum1, expected1);

