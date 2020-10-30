### 思路1 直接从左往右加

因为输入的链表和我们正常计数的方向是反着的，我们直接从左往右加，正好就是从个位开始算。另外用carry来处理进位。

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        pre_head = p = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            v1, v2 = 0, 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, current = divmod(v1 + v2 + carry, 10)
            p.next = ListNode(current)
            p = p.next
        return pre_head.next
```