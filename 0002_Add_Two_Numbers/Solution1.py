from utils_py.list import *


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        p = dummy
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            cur_sum = v1 + v2 + carry
            new_node = ListNode(cur_sum % 10)
            carry = cur_sum // 10
            p.next = new_node
            p = p.next
        return dummy.next


def test(test_name, l1, l2, expected):
    res = Solution().addTwoNumbers(l1, l2)
    if is_equal_list(res, expected):
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    l11 = ListNode(2)
    l11.next = ListNode(4)
    l11.next.next = ListNode(3)

    l21 = ListNode(5)
    l21.next = ListNode(6)
    l21.next.next = ListNode(4)

    expected1 = ListNode(7)
    expected1.next = ListNode(0)
    expected1.next.next = ListNode(8)

    test('test1', l11, l21, expected1)

    l12 = ListNode(5)
    l22 = ListNode(5)

    expected2 = ListNode(0)
    expected2.next = ListNode(1)
    test('test2', l12, l22, expected2)
