from utils_py.list import *


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None

        dummy = ListNode(0)
        dummy.next = head
        p = dummy

        for _ in range(m):
            node_before = p
            p = p.next

        pm = p
        next = None  # after for, next is node after
        pre = None   # after for pre is last node between

        # n - m + 1 即是中间链表的节点数
        for _ in range(n - m + 1):
            next = p.next
            p.next = pre
            pre = p
            p = next

        node_before.next = pre
        pm.next = next
        return dummy.next


def test(test_name, head, m, n, expected):
    res = Solution().reverseBetween(head, m, n)
    print_list(res, 5)
    if is_equal_list(res, expected):
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    head1 = ListNode(1)
    head1.next = ListNode(2)
    head1.next.next = ListNode(3)
    head1.next.next.next = ListNode(4)
    head1.next.next.next.next = ListNode(5)
    m1, n1 = 2, 4
    expected1 = ListNode(1)
    expected1.next = ListNode(4)
    expected1.next.next = ListNode(3)
    expected1.next.next.next = ListNode(2)
    expected1.next.next.next.next = ListNode(5)
    test('test1', head1, m1, n1, expected1)

# Reverse a linked list from position m to n. Do it in one-pass.
#
# Note: 1 ≤ m ≤ n ≤ length of list.
#
# Example:
#
# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL