from typing import List
from util_py.list import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1, p2 = l1, l2
        dummy_head = ListNode(0)
        p = dummy_head
        carry = 0

        while p1 or p2 or carry:
            v1, v2 = 0, 0
            if p1:
                v1 = p1.val
                p1 = p1.next
            if p2:
                v2 = p2.val
                p2 = p2.next

            cur_sum = v1 + v2 + carry
            carry = (cur_sum) // 10
            new_node = ListNode((cur_sum) % 10)
            p.next = new_node
            p = p.next

        return dummy_head.next


def test(test_name, l1, l2, expected):
    res = Solution().addTwoNumbers(l1, l2)
    if is_equal_list(res, expected):
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    l11 = build_list([7,1,6])
    l21 = build_list([5,9,2])
    expected1 = build_list([2,1,9])
    test('test1', l11, l21, expected1)

    l12 = build_list([5])
    l22 = build_list([5])
    expected2 = build_list([0,1])
    test('test2', l12, l22, expected2)


# You have two numbers represented by a linked list,
# where each node contains a single digit. The digits are 
# stored in reverse order, such that the 1's digit is at the 
# head of the list. Write a function that adds the two numbers 
# and returns the sum as a linked list.

# Example:

# Input: (7 -> 1 -> 6) + (5 -> 9 -> 2). That is, 617 + 295.
# Output: 2 -> 1 -> 9. That is, 912.

# Follow Up: Suppose the digits are stored in forward order.
#  Repeat the above problem.

# Example:

# Input: (6 -> 1 -> 7) + (2 -> 9 -> 5). That is, 617 + 295.
# Output: 9 -> 1 -> 2. That is, 912.
