## 思路1 遍历即可

```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode head(0);
        ListNode *p = &head;
        while (l1 || l2) {
            int v1, v2;
            v1 = l1 ? l1->val : INT_MAX;
            v2 = l2 ? l2->val : INT_MAX;
            if (v1 < v2) {
                p->next = l1;
                l1 = l1->next;
            } else {
                p->next = l2;
                l2 = l2->next;
            }
            p = p->next;
        }
        return head.next;
    }
};
```

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = p = ListNode(-1)
        while l1 and l2:            # 使用原有的结点，而不是新创建结点
            v1, v2 = l1.val, l2.val
            if v1 < v2:
                p.next = l1
                p = p.next
                l1 = l1.next
            else:
                p.next = l2
                p = p.next
                l2 = l2.next
        if l1:              # 这两个if只有一个会发生
            p.next = l1
        if l2:
            p.next = l2
        return dummy_head.next
```