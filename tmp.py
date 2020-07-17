from utils_py.list import *

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p1, p2 = head, head
        for _ in range(n):
            p1 = p1.next

        # 唯一需要处理的特殊情况，即n == 链表长度
        if not p1:
            return head.next

        while p1.next:
            p1 = p1.next
            p2 = p2.next
        
        p2.next = p2.next.next
        return head


def test(test_name, head, n, expected):
    res = Solution().removeNthFromEnd(head, n)
    if is_equal_list(res, expected):
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')



if __name__ == '__main__':

    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(3)
    list1.next.next.next = ListNode(4)
    list1.next.next.next.next = ListNode(5)
    n1 = 2
    expected1 = ListNode(1)
    expected1.next = ListNode(2)
    expected1.next.next = ListNode(3)
    expected1.next.next.next = ListNode(5)
    test("test1", list1, n1, expected1)

    list2 = ListNode(1)
    n2 = 1
    expected2 = None
    test("test2", list2, n2, expected2)

    list3 = ListNode(1)
    list3.next = ListNode(2)
    n3 = 2
    expected3 = ListNode(2)
    test("test3", list3, n3, expected3)


# Given a linked list, remove the n-th node from the end of list
# and return its head.
#
# Example:
#
# Given linked list: 1.2.3.4.5, and n = 2.
#
# After removing the second node from the end, the linked list
#  becomes 1.2.3.5.
#
# Note:
#
# Given n will always be valid.
#
# Follow up:
#
# Could you do this in one pass?