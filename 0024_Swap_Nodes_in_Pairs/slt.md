### 思路1 直接两两交换

cpp中我们用指针的指针来防止断链。`*pp == a -> b -> (b->next)` to `*pp == b -> a -> (b->next)`

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
    ListNode* swapPairs(ListNode* head) {
        ListNode **pp = &head;
        ListNode *a, *b;
        while((a = *pp) && (b = a->next)){
            a->next = b->next;
            b->next = a;
            // 防止断链，一开始*pp是head，这里就相当于head = b;
            // 对于后面的结点来说，上面一对的next指向*pp，让*pp = b，就让前面一对的next指向了b
            *pp = b;
            pp = &(a->next);
        }
        return head;
    }
};
```


python中赋值很方便，我们直接用一个pre来记录前一个结点
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