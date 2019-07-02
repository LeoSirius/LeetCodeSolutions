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
        ListNode *head = new ListNode(0);
        ListNode *p = head;
        while(l1 && l2){
            ListNode *small;
            if(l1->val < l2->val){
                small = l1;
                l1 = l1->next;
            }else{
                small = l2;
                l2 = l2->next;
            }
            p->next = small;
            p = p->next;
        }
        while(l1){
            p->next = l1;
            p = p->next;
            l1 = l1->next;
        }
        while(l2){
            p->next = l2;
            p = p->next;
            l2 = l2->next;
        }
        return head->next;
    }
};
```

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = p = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                p.next = ListNode(l1.val)
                l1 = l1.next
            else:
                p.next = ListNode(l2.val)
                l2 = l2.next
            p = p.next
        while l1:
            p.next = ListNode(l1.val)
            p = p.next
            l1 = l1.next
        while l2:
            p.next = ListNode(l2.val)
            p = p.next
            l2 = l2.next
        return root.next
```