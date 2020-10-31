class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def in_order(node, in_list):
    if not node:
        return
    in_order(node.left, in_list)
    in_list.append(node.val)
    in_order(node.right, in_list)

def get_inorder_list(tree):
    in_list = []
    in_order(tree, in_list)
    return in_list


def is_equal_tree(t1, t2):
    if not t1 and not t2:
        return True
    if not t1 or not t2:
        return False
    if t1.val != t2.val:
        return False
    return is_equal_tree(t1.left, t2.left) and is_equal_tree(t1.right, t2.right)
