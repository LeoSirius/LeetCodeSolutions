from util_py.list import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None

        pre = ListNode(0)
        pre.next = head
        p = pre

        while p and p.next:
            while p and p.next and p.next.val == val:
                p.next = p.next.next
            p = p.next
        return pre.next


def test(test_name, head, val, expected):
    res = Solution().removeElements(head, val)
    if is_equal_list(res, expected):
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    head1 = build_list([1,2,6,3,4,5,6])
    val1 = 6
    expected1 = build_list([1,2,3,4,5])
    test('test1', head1, val1, expected1)

    head2 = None
    val2 = 1
    expected2 = None
    test('test2', head2, val2, expected2)

    head3 = build_list([7,7,7,7])
    val3 = 7
    expected3 = None
    test('test3', head3, val3, expected3)
