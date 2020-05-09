from typing import List

from utils_py.tree import *


class Solution:

    inorder = []
    postorder = []

    def build(self, s1, e1, s2, e2):
        root_val = self.postorder[e2]
        root_idx = s1
        for i in range(s1, e1+1):
            if self.inorder[i] == root_val:
                root_idx = i
                break

        new_node = TreeNode(root_val)
        
        left_cnt = root_idx - s1
        right_cnt = e1 - root_idx

        if left_cnt > 0:
            new_node.left = self.build(s1, root_idx - 1, s2, s2 + left_cnt - 1)
        if right_cnt > 0:
            new_node.right = self.build(root_idx + 1, e1, s2 + left_cnt, e2 - 1)
        return new_node


    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return None
        self.inorder = inorder
        self.postorder = postorder
        size = len(inorder)
        return self.build(0, size-1, 0, size-1)


def test(test_name, inorder, postorder, expected):
    res = Solution().buildTree(inorder, postorder)
    if is_same_tree(res, expected):
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == "__main__":
    inorder1 = [9,3,15,20,7]
    postorder1 = [9,15,7,20,3]
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
    test('test1', inorder1, postorder1, expected1)


    inorder2 = []
    postorder2 = []
    expected2 = None
    test('test2', inorder2, postorder2, expected2)