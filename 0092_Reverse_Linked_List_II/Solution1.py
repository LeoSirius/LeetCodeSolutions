from util_py.list import *

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head:
            return None

        dummy = ListNode(0)
        dummy.next = head
        p = dummy

        # after this loop, node_before is node before [left, right], p is first node in between
        for _ in range(left):
            node_before = p
            p = p.next

        # after next loop, p_left is pointer to left, pre is pointer to right node_after is next node after between
        p_left = p
        node_after, pre = None, None

        # right - left + 1 = total nodes count in between
        for _ in range(right - left + 1):
            node_after = p.next
            p.next = pre
            pre = p
            p = node_after

        node_before.next = pre
        p_left.next = node_after
        return dummy.next


def test(test_name, head, m, n, expected):
    res = Solution().reverseBetween(head, m, n)
    if is_equal_list(res, expected):
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    head1 = build_list([1,2,3,4,5])
    left1, right1 = 2, 4
    expected1 = build_list([1,4,3,2,5])
    test('test1', head1, left1, right1, expected1)

# Reverse a linked list from position m to n. Do it in one-pass.
#
# Note: 1 ≤ m ≤ n ≤ length of list.
#
# Example:
#
# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL
