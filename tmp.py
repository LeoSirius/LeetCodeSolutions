from utils_py.list import *

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not k:
            return head
        length = 1
        p1, p2 = head, head

        while p1.next:
            length += 1
            p1 = p1.next
        p1.next = head

        k %= length
        right_len = length - k
        while right_len - 1 > 0:   # p2移动right_len - 1个位置，即新头结点的前一个位置
            p2 = p2.next
            right_len -= 1

        new_head, p2.next = p2.next, None

        return new_head


def test(test_name, head, k, expected):
    res = Solution().rotateRight(head, k)
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
    k1 = 2
    expected1 = ListNode(4)
    expected1.next = ListNode(5)
    expected1.next.next = ListNode(1)
    expected1.next.next.next = ListNode(2)
    expected1.next.next.next.next = ListNode(3)
    test("test1", head1, k1, expected1)


    head2 = ListNode(0)
    head2.next = ListNode(1)
    head2.next.next = ListNode(2)
    k2 = 4
    expected2 = ListNode(2)
    expected2.next = ListNode(0)
    expected2.next.next = ListNode(1)
    test("test2", head2, k2, expected2)


    head3 = None
    k3 = 0
    expected3 = None
    test("test3", head3, k3, expected3)


    head4 = ListNode(1)
    head4.next = ListNode(2)
    k4 = 0
    expected4 = ListNode(1)
    expected4.next = ListNode(2)
    test("test4", head4, k4, expected4)

    head5 = ListNode(1)
    head5.next = ListNode(2)
    k5 = 1
    expected5 = ListNode(2)
    expected5.next = ListNode(1)
    test("test5", head5, k5, expected5)

# Given a linked list, rotate the list to the right by k places, where k is non-negative.
#
# Example 1:
#
# Input: 1->2->3->4->5->NULL, k = 2
# Output: 4->5->1->2->3->NULL
# Explanation:
# rotate 1 steps to the right: 5->1->2->3->4->NULL
# rotate 2 steps to the right: 4->5->1->2->3->NULL

# Example 2:
#
# Input: 0->1->2->NULL, k = 4
# Output: 2->0->1->NULL
# Explanation:
# rotate 1 steps to the right: 2->0->1->NULL
# rotate 2 steps to the right: 1->2->0->NULL
# rotate 3 steps to the right: 0->1->2->NULL
# rotate 4 steps to the right: 2->0->1->NULL