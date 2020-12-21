from typing import List

from utils_py.tree import *

class Solution:
    def gen(self, start, end):
        root_lst = []
        if start > end:
            root_lst.append(None)
        
        for i in range(start, end + 1):
            root_left_lst = self.gen(start, i-1)
            root_right_lst = self.gen(i+1, end)
            for l in root_left_lst:
                for r in root_right_lst:
                    new_root = TreeNode(i)
                    new_root.left = l
                    new_root.right = r
                    root_lst.append(new_root)
        return root_lst


    def generateTrees(self, n: int) -> List[TreeNode]:
        if not n:
            return []
        return self.gen(1, n)


def test(test_name, n, expected):
    res = Solution().generateTrees(n)
    same_cnt = 0
    for i in res:
        for j in expected:
            if is_equal_tree(i, j):
                same_cnt += 1
    if same_cnt == len(res):
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == "__main__":
    n1 = 3
    t1 = TreeNode(1)
    t1.right = TreeNode(3)
    t1.right.left = TreeNode(2)
    t2 = TreeNode(3)
    t2.left = TreeNode(2)
    t2.left.left = TreeNode(1)
    t3 = TreeNode(3)
    t3.left = TreeNode(1)
    t3.left.right = TreeNode(2)
    t4 = TreeNode(2)
    t4.left = TreeNode(1)
    t4.right = TreeNode(3)
    t5 = TreeNode(1)
    t5.right = TreeNode(2)
    t5.right.right = TreeNode(3)
    expected1 = [t1,t2,t3,t4,t5]
    test('test1', n1, expected1)
