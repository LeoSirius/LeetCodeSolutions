from typing import List
from utils_py.tree import *

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        que = [root]

        while que:
            size = len(que)
            row = []
            while size:
                size -= 1
                p = que.pop(0)
                row.append(p.val)
                if p.left:
                    que.append(p.left)
                if p.right:
                    que.append(p.right)
            res.append(row)
        return list(reversed(res))


def test(test_name, root, expected):
    res = Solution().levelOrderBottom(root)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    #    3
    #    / \
    #   9  20
    #     /  \
    #    15   7
    expected1 = [
        [15,7],
        [9,20],
        [3]
    ]
    test('test1', root1, expected1)
