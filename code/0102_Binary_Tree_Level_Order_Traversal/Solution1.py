from typing import List
from utils_py.tree import *
import queue

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        que = []
        if not root:
            return que
        que.append(root)
        res = []

        while que:
            cnt = len(que)
            row = []
            while cnt:
                cnt -= 1
                p = que.pop(0)
                row.append(p.val)
                if p.left:
                    que.append(p.left)
                if p.right:
                    que.append(p.right)
            res.append(row)
        return res

def test(test_name, root, expected):
    res = Solution().levelOrder(root)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == "__main__":
    t1 = TreeNode(3);
    t1.left = TreeNode(9);
    t1.right = TreeNode(20);
    t1.right.left = TreeNode(15);
    t1.right.right = TreeNode(7);
    expected1 = [
        [3], [9, 20], [15, 7]
    ]
    #      3
    #     / \
    #    9  20
    #      /  \
    #     15   7
    test("test1", t1, expected1);

    t2 = None
    expected2 = []
    test("test2", t2, expected2);

