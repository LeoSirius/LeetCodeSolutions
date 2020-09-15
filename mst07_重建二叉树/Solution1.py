from typing import *

from utils_py.tree import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        size = len(preorder)
        if not size or (len(preorder) != len(inorder)):
            return None

        def build_tree(s1: int, e1: int, s2: int, e2: int):
            root_val = preorder[s1]
            new_root = TreeNode(root_val)

            root_idx_in = s2
            for i in range(s2, e2 + 1):
                if inorder[i] == root_val:
                    root_idx_in = i
                    break
            
            left_count = root_idx_in - s2
            right_count = e2 - root_idx_in
            if left_count:
                new_root.left = build_tree(s1 + 1, s1 + left_count, s2, root_idx_in - 1)
            if right_count:
                new_root.right = build_tree(s1 + left_count + 1, e1, root_idx_in + 1, e2)
            return new_root
        
        res = build_tree(0, size-1, 0, size-1)
        return res


def test(test_name, preorder, inorder, expected):
    res = Solution().buildTree(preorder, inorder)
    if is_equal_tree(res, expected):
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == "__main__":
    preorder1 = [3,9,20,15,7]
    inorder1 = [9,3,15,20,7]
    #     3
    #    / \
    #   9  20
    #     /  \
    #    15   7
    expected1 = TreeNode(3)
    expected1.left = TreeNode(9)
    expected1.right = TreeNode(20)
    expected1.right.left = TreeNode(15)
    expected1.right.right = TreeNode(7)
    test("test1", preorder1, inorder1, expected1);



# 输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。A
# 假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

# 例如，给出

# 前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]

# 返回如下的二叉树：

#     3
#    / \
#   9  20
#     /  \
#    15   7

# 限制：

# 0 <= 节点个数 <= 5000