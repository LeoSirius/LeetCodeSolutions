class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def is_same_tree(t1, t2):
    if not t1 and not t2:
        return True
    if not t1 or not t2:
        return False
    if t1.val != t2.val:
        return False
    return is_same_tree(t1.left, t2.left) and is_same_tree(t1.right, t2.right)
