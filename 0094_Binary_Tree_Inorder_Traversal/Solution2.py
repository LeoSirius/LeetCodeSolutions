from typing import List

from utils_py.tree import *

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        p = root
        stk = []
        res = []
        while p or stk:
            while p:
                stk.append(p)
                p = p.left
            p = stk.pop()
            res.append(p.val)
            p = p.right
        return res

def test(test_name, root, expected):
    res = Solution().inorderTraversal(root)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == "__main__":
    root1 = TreeNode(1)
    root1.right = TreeNode(2)
    root1.right.left = TreeNode(3)
    expected1 = [1,3,2]

    test('test1', root1, expected1)


