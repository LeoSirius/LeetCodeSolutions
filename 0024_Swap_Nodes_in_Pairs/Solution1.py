from utils_py.list import *


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        while pre.next and pre.next.next:
            n1, n2 = pre.next, pre.next.next

            pre.next = n2
            nnext = n2.next
            n2.next = n1
            n1.next = nnext
            # python 其可以写成一行
            # pre.next, n2.next, n1.next = n2, n1, n2.next
            pre = n1
        return dummy.next


def test(test_name, head, expected):
    res = Solution().swapPairs(head)
    if is_equal_list(res, expected):
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    head1 = ListNode(1)
    head1.next = ListNode(2)
    head1.next.next = ListNode(3)
    head1.next.next.next = ListNode(4)

    expected1 = ListNode(2)
    expected1.next = ListNode(1)
    expected1.next.next = ListNode(4)
    expected1.next.next.next = ListNode(3)

    test('test1', head1, expected1)


# Given a linked list, swap every two adjacent nodes and return its head.
#
# You may not modify the values in the list's nodes, only nodes itself may be changed.
#
#  
#
# Example:
#
# Given 1->2->3->4, you should return the list as 2->1->4->3.
