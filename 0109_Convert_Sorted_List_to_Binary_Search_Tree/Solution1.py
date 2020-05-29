from utils_py.tree import *
from utils_py.list import *

class Solution:
    def build_tree(self, head, tail):
        if head == tail:
            return
        slow = head
        fast = head
        while fast != tail and fast.next != tail:
            slow = slow.next
            fast = fast.next.next
        new_node = TreeNode(slow.val)
        new_node.left = self.build_tree(head, slow)
        new_node.right = self.build_tree(slow.next, tail)
        return new_node

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
