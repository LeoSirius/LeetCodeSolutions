from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def _gen(self, start, end):
        root_list = []
        if (start > end):
            root_list.append(None)

        for i in range(start, end + 1):
            left_root_list = self._gen(start, i - 1)
            right_root_list = self._gen(i + 1, end)
            for l_root in left_root_list:
                for r_root in right_root_list:
                    new_root = TreeNode(i)
                    new_root.left = l_root
                    new_root.right = r_root
                    root_list.append(new_root)

        return root_list

    def generateTrees(self, n: int) -> List[TreeNode]:
        if not n:
            return []
        return self._gen(1, n)
        

def is_same_tree(root1: TreeNode, root2: TreeNode) -> bool:
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    if root1.val != root2.val:
        return False
    return is_same_tree(root1.left, root2.left) and is_same_tree(root1.right, root2.right)


def test(test_name, n, expected):
    res = Solution().generateTrees(n)
    same_cnt = 0
    for t1 in res:
        for t2 in expected:
            if is_same_tree(t1, t2):
                same_cnt += 1
    if same_cnt == len(res):
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    n1 = 3

    root1 = TreeNode(1)
    root1.right = TreeNode(3)
    root1.right.left = TreeNode(2)

    root2 = TreeNode(3)
    root2.left = TreeNode(2)
    root2.left.left = TreeNode(1)

    root3 = TreeNode(3)
    root3.left = TreeNode(1)
    root3.left.right = TreeNode(2)

    root4 = TreeNode(2)
    root4.left = TreeNode(1)
    root4.right = TreeNode(3)

    root5 = TreeNode(1)
    root5.right = TreeNode(2)
    root5.right.right = TreeNode(3)

    expected1 = [root1, root2, root3, root4, root5]
    test('test1', n1, expected1)
