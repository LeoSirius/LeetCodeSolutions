from utils_py.tree import *

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = ''
        if not root:
            return 'null'   # 注意这里不能返回空串

        que = [root]
        while que:
            p = que.pop(0)
            if p:
                res += str(p.val) + ','
                que.append(p.left)
                que.append(p.right)
            else:
                res += 'null,'
        return res[:-1]

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        dummy = TreeNode(0)
        que = [dummy]
        left_child = False

        for val_str in data.split(','):
            node = None if val_str == 'null' else TreeNode(int(val_str))
            p = que[0] # 注意这里没有pop，在左右子树都接上后，再pop
            if left_child:
                p.left = node
            else:
                p.right = node
                que.pop(0)
            
            if node:
                que.append(node)
            
            left_child = not left_child

        return dummy.right

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

def test1():
    #     1
    #    / \
    #   2   3
    #      / \
    #     4   5

    # 序列化为 "[1,2,3,null,null,4,5]"
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.right.left = TreeNode(4)
    tree.right.right = TreeNode(5)
    codec = Codec()
    res_tree = codec.deserialize(codec.serialize(tree))
    if is_equal_tree(res_tree, tree):
        print('test1 success.')
    else:
        print('test1 failed.')


def test2():
    tree = None
    codec = Codec()
    res_tree = codec.deserialize(codec.serialize(tree))
    if is_equal_tree(res_tree, tree):
        print('test2 success.')
    else:
        print('test2 failed.')

if __name__ == "__main__":
    test1()
    test2()
