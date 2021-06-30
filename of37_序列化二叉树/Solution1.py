from collections import deque

from util_py.tree import *


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        items = []
        dq = deque([root])
        while dq:
            cur_node = dq.popleft()
            items.append(str(cur_node.val) if cur_node else 'null')
            if cur_node:
                dq.append(cur_node.left)
                dq.append(cur_node.right)
        return ','.join(items) if items else 'null'


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        items = data.split(',')
        dummy = TreeNode(0)
        dq = deque([dummy])

        is_left = False
        for item in items:
            node = None if item == 'null' else TreeNode(int(item))
            q = dq[0]
            if is_left:
                q.left = node
            else:
                q.right = node
                dq.popleft()
            if node:
                dq.append(node)
            is_left = not is_left
        return dummy.right


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))


def test1():
    #     1
    #    / \
    #   2   3
    #      / \
    #     4   5

    # 序列化为 "1,2,3,null,null,4,5"
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.right.left = TreeNode(4)
    tree.right.right = TreeNode(5)
    codec = Codec()
    res_tree = codec.deserialize(codec.serialize(tree))
    if is_equal_tree(res_tree, tree):
        print('test1 succeed')
    else:
        print('test1 fail')


def test2():
    tree = None
    codec = Codec()
    res_tree = codec.deserialize(codec.serialize(tree))
    if is_equal_tree(res_tree, tree):
        print('test2 succeed')
    else:
        print('test2 fail')

if __name__ == "__main__":
    test1()
    test2()
