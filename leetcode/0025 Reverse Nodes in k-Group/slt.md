### 思路1 k个分别反转，迭代实现

关键是理清各个结点的指向

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = jump = ListNode(0)
        dummy.next = l = r = head

        while True:
            count = 0
            while r and count < k:
                count += 1
                r = r.next
            if count == k:
                pre, cur = l, r
                for _ in range(k):
                    tmp = cur.next
                    cur.next = pre
                    pre = cur
                    cur = tmp
                jump.next = pre
                jump = l
                l = r
            else:
                # 剩下的结点不到k个
                return dummy.next
```