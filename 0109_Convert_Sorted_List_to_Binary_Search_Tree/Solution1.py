from utils_py.list import *
from utils_py.tree import *

class Solution:
    def build_tree(self, head, tail):
        if head == tail: return

        slow, fast = head, head
        # 这个while第一次调用后，slow指向0， fast是None
        while fast != tail and fast.next != tail:
            fast = fast.next.next
            slow = slow.next
        tree_node = TreeNode(slow.val)
        tree_node.left = self.build_tree(head, slow)
        tree_node.right = self.build_tree(slow.next, tail)
        return tree_node


    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # 左闭右开
        return self.build_tree(head, None)


def test(test_name, head, expected_arr):
    # 这道题不要用is_equal_tree来测试，答案不唯一。但是他们的中序遍历的结果一定是唯一的
    res = Solution().sortedListToBST(head)
    in_list = get_inorder_list(res)
    if in_list == expected_arr:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    head1 = ListNode(-10)
    head1.next = ListNode(-3)
    head1.next.next = ListNode(0)
    head1.next.next.next = ListNode(5)
    head1.next.next.next.next = ListNode(9)
    expected_arr1 = [-10,-3,0,5,9]
    #       0
    #      / \
    #    -3   9
    #    /   /
    #  -10  5
    test('test1', head1, expected_arr1)


# Given a singly linked list where elements are sorted in ascending order,
# convert it to a height balanced BST.
#
# For this problem, a height-balanced binary tree is defined as a binary
# tree in which the depth of the two subtrees of every node never differ by more than 1.
