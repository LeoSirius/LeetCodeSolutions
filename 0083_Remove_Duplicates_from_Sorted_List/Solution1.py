from utils_py.list import *


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        p = head
        while p and p.next:
            while p.next and p.val == p.next.val:
                p.next = p.next.next
            p = p.next
        return head


def test(test_name, head, expected):
    res = Solution().deleteDuplicates(head)
    print_list(res)
    if is_equal_list(res, expected):
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    head1 = ListNode(1)
    head1.next = ListNode(1)
    head1.next.next = ListNode(2)
    expected1 = ListNode(1)
    expected1.next = ListNode(2)
    test('test1', head1, expected1)

    head2 = ListNode(1)
    head2.next = ListNode(1)
    head2.next.next = ListNode(1)
    head2.next.next.next = ListNode(2)
    head2.next.next.next.next = ListNode(3)
    expected2 = ListNode(1)
    expected2.next = ListNode(2)
    expected2.next.next = ListNode(3)
    test('test2', head2, expected2)


# Given a sorted linked list, delete all duplicates such that each element appear only once.
#
# Example 1:
#
# Input: 1->1->2
# Output: 1->2
# Example 2:
#
# Input: 1->1->2->3->3
# Output: 1->2->3
