# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode(0)
        p = dummy_head
        carry = 0
        while l1 or l2 or carry:
            v1, v2 = 0, 0
            if l1: 
                v1 = l1.val
                l1 = l1.next
            if l2: 
                v2 = l2.val
                l2 = l2.next
            s = v1 + v2 + carry
            p.next = ListNode(s % 10)
            p = p.next
            carry = s // 10
        return dummy_head.next
