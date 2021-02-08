from typing import *

from utils_py.tree import TreeNode

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root: return res

        que = [root]
        left2right = True
        while len(que):
            cur_size = len(que)
            row = []
            while cur_size:
                p = que.pop(0)
                row.append(p.val)
                if p.left: que.append(p.left)
                if p.right: que.append(p.right)
                cur_size -= 1
            if not left2right:
                row.reverse()
            left2right = not left2right
            res.append(row)
        return res


def test(test_name, root, expected):
    res = Solution().levelOrder(root)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    #   3
    #  / \
    # 9  20
    #   /  \
    #  15   7
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    expected1 = [
        [3],
        [20,9],
        [15,7]
    ]
    test("test1", root1, expected1)