from typing import List
from utils_py.tree import *

class Solution:
    def build(self, s1, e1, s2, e2, preor, inor):
        rootval = preor[s1]
        rootidx_in_inor = inor.index(rootval)
        new_node = TreeNode(rootval)

        left_cnt = rootidx_in_inor - s2
        right_cnt = e2 - rootidx_in_inor
        if left_cnt > 0:
            new_node.left = self.build(s1+1, s1+1+left_cnt-1, s2, rootidx_in_inor-1, preor, inor)
        if right_cnt > 0:
            new_node.right = self.build(s1+1+left_cnt, e1, rootidx_in_inor+1, e2, preor, inor)
        return new_node


    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not input:
            return None
        return self.build(0, len(preorder)-1, 0, len(inorder)-1, preorder, inorder)

def test(test_name, preorder, inorder, expected):
    res = Solution().buildTree(preorder, inorder)
    if is_same_tree(res, expected):
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == "__main__":
    #  preorder = [3,9,20,15,7]
    #  inorder = [9,3,15,20,7]
    #  Return the following binary tree:
    #      3
    #     / \
    #    9  20
    #      /  \
    #     15   7
    pre1 = [3,9,20,15,7];
    in1 = [9,3,15,20,7];
    expected1 = TreeNode(3)
    expected1.left = TreeNode(9)
    expected1.right = TreeNode(20)
    expected1.right.left = TreeNode(15)
    expected1.right.right = TreeNode(7)
    test("test1", pre1, in1, expected1);

    pre2 = [];
    in2 = [];
    expected2 = None;
    test("test2", pre2, in2, expected2);
