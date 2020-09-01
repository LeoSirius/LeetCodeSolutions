from utils_py.list import *


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        pre, p = dummy, head
        while p and p.next:
            # 分成是dup和不是dup两种情况，如果不是dup，直接后移
            if p.val == p.next.val:
                after_same = p
                while after_same and after_same.val == p.val:
                    after_same = after_same.next
                pre.next = after_same
                p = after_same
                continue
            pre = pre.next
            p = p.next

        return dummy.next


def test(test_name, head, expected):
    res = Solution().deleteDuplicates(head)
    if is_equal_list(res, expected):
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    head1 = ListNode(1)
    head1.next = ListNode(2)
    head1.next.next = ListNode(3)
    head1.next.next.next = ListNode(3)
    head1.next.next.next.next = ListNode(4)
    head1.next.next.next.next.next = ListNode(4)
    head1.next.next.next.next.next.next = ListNode(5)
    expected1 = ListNode(1)
    expected1.next = ListNode(2)
    expected1.next.next = ListNode(5)
    test('test1', head1, expected1)

    head2 = ListNode(1)
    head2.next = ListNode(1)
    head2.next.next = ListNode(1)
    head2.next.next.next = ListNode(2)
    head2.next.next.next.next = ListNode(3)
    expected2 = ListNode(2)
    expected2.next = ListNode(3)
    test('test2', head2, expected2)


# Given a sorted linked list, delete all nodes that have duplicate numbers,
# leaving only distinct numbers from the original list.
#
# Return the linked list sorted as well.
#
# Example 1:
#
# Input: 1->2->3->3->4->4->5
# Output: 1->2->5
# Example 2:
#
# Input: 1->1->1->2->3
# Output: 2->3

