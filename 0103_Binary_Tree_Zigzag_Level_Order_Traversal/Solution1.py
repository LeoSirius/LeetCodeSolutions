from typing import *
from utils_py.tree import *

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        que = []
        res = []
        p = root
        level = 0
        que.append(p)
        while que:
            cur_level_size = len(que)
            row = []
            level += 1
            while cur_level_size:
                cur_level_size -= 1
                p = que.pop(0)
                row.append(p.val)
                if p.left:
                    que.append(p.left)
                if p.right:
                    que.append(p.right)
            if level % 2 == 0:
                res.append(list(reversed(row)))
            else:
                res.append(row)
        return res


def test(test_name, root, expected):
    res = Solution().zigzagLevelOrder(root)
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
        [3],
        [20, 9],
        [15, 7]
    ];
    #      3
    #     / \
    #    9  20
    #      /  \
    #     15   7
    test("test1", t1, expected1);

    t2 = None
    expected2 = []
    test("test2", t2, expected2)