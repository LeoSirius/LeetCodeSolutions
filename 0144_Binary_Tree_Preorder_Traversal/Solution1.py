from typing import *
from utils_py.tree import *

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res

        p = root
        stk = []
        while p or stk:
            while p:
                res.append(p.val)
                stk.append(p)
                p = p.left
            p = stk.pop()
            p = p.right
        return res


def test(test_name, root, expected):
    res = Solution().preorderTraversal(root)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    # 1
    #  \
    #   2
    #  /
    # 3
    root1 = TreeNode(1);
    root1.right = TreeNode(2);
    root1.right.left = TreeNode(3);
    expected1 = [1,2,3];
    test("test1", root1, expected1);

    root2 = TreeNode(1);
    root2.left = TreeNode(2);
    expected2 = [1,2];
    test("test2", root2, expected2);
