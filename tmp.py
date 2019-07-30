# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = p = ListNode(0)
        carry = 0
        while carry or l1 or l2:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, v = divmod(carry + v1 + v2, 10)
            p.next = ListNode(v)
            p = p.next
        return dummy_head.next