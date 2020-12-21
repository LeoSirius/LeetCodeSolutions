from utils_py.list import *

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy_small, dummy_large = ListNode(0), ListNode(0)
        p = head
        p_s, p_l = dummy_small, dummy_large
        while p:
            if p.val < x:
                p_s.next = p
                p_s = p_s.next
            else:
                p_l.next = p
                p_l = p_l.next
            p = p.next
            # 最后把它们原来尾部清空
            if not p:
                p_s.next = None
                p_l.next = None

        p = dummy_small
        while p.next: p = p.next
        p.next = dummy_large.next

        return dummy_small.next


def test(test_name, head, x, expected):
    res = Solution().partition(head, x)
    if is_equal_list(res, expected):
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == '__main__':
    head1 = ListNode(1)
    head1.next = ListNode(4)
    head1.next.next = ListNode(3)
    head1.next.next.next = ListNode(2)
    head1.next.next.next.next = ListNode(5)
    head1.next.next.next.next.next = ListNode(2)
    x = 3
    expected1 = ListNode(1)
    expected1.next = ListNode(2)
    expected1.next.next = ListNode(2)
    expected1.next.next.next = ListNode(4)
    expected1.next.next.next.next = ListNode(3)
    expected1.next.next.next.next.next = ListNode(5)
    test('test1', head1, x, expected1)



# Given a linked list and a value x, partition it such that all
# nodes less than x come before nodes greater than or equal to x.
#
# You should preserve the original relative order of the nodes in each of the two partitions.
#
# Example:
#
# Input: head = 1->4->3->2->5->2, x = 3
# Output: 1->2->2->4->3->5
