from utils_py.tree import *


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stk = []
        self.p = root

    def next(self) -> int:
        """
        @return the next smallest number
        """
        while self.p:
            self.stk.append(self.p)
            self.p = self.p.left

        res = self.stk.pop()
        self.p = res.right

        return res.val


    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return bool(self.stk) or bool(self.p)



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()


def test1():
    #      7
    #     / \
    #    3   15
    #       /  \
    #      9    20
    root = TreeNode(7);
    root.left = TreeNode(3);
    root.right = TreeNode(15);
    root.right.left = TreeNode(9);
    root.right.right = TreeNode(20);

    iter = BSTIterator(root);
    res1 = iter.next();      # 3
    res2 = iter.next();      # 7
    res3 = iter.hasNext();   # true
    res4 = iter.next();      # 9
    res5 = iter.hasNext();   # true
    res6 = iter.next();      # 15
    res7 = iter.hasNext();   # true
    res8 = iter.next();      # 20
    res9 = iter.hasNext();   # false
    print((res1, res2, res3, res4, res5, res6, res7, res8, res9))
    if (res1, res2, res3, res4, res5, res6, res7, res8, res9) == (
          3, 7, True, 9, True, 15, True, 20, False):
        print('test1 success.')
    else:
        print('test1 failed.')


if __name__ == "__main__":
    test1()



# Implement an iterator over a binary search tree (BST). 
# Your iterator will be initialized with the root node of a BST.

# Calling next() will return the next smallest number in the BST.

# Example:

# BSTIterator iterator = new BSTIterator(root);
# iterator.next();    // return 3
# iterator.next();    // return 7
# iterator.hasNext(); // return true
# iterator.next();    // return 9
# iterator.hasNext(); // return true
# iterator.next();    // return 15
# iterator.hasNext(); // return true
# iterator.next();    // return 20
# iterator.hasNext(); // return false
#  

# Note:

# next() and hasNext() should run in average O(1) time and uses O(h) memory,
# where h is the height of the tree.
# You may assume that next() call will always be valid, that is,
# there will be at least a next smallest number in the BST when next() is called.