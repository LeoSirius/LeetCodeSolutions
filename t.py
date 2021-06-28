from util_py.list import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


def test(test_name, head, expected):
    res = Solution().hasCycle(head)
    if type(res) == type(expected) and res == expected:
        print(test_name + ' succeed')
    else:
        print(test_name + ' fail')


if __name__ == '__main__':
    head1 = build_list([3,2,0,-4])
    head1.next.next.next.next = head1.next
    expected1 = True
    test('test1', head1, expected1)

    head2 = build_list([1,2])
    head2.next.next = head2
    expected2 = True
    test('test2', head2, expected2)

    head3 = build_list([1])
    expected3 = False
    test('test3', head3, expected3)
