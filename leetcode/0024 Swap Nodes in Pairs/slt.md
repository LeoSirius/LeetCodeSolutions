### 思路1 直接两两交换

`pre -> a -> b -> b.next` to `pre -> b -> a -> b.next`

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        pre, pre.next = ListNode(0), head
        dummy_head = pre
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return dummy_head.next
```