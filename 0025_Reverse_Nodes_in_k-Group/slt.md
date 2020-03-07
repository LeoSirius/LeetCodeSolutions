### 思路1 k个分别反转，迭代实现

关键是理清各个结点的指向

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
    ListNode* reverseKGroup(ListNode* head, int k) {
        if(head == nullptr || k == 1) return head;
        ListNode *dummy_head = new ListNode(-1);
        dummy_head->next = head;
        ListNode *jump = dummy_head;
        ListNode *l, *r, *pre, *cur;
        l = r = head;

        while(true){
            int count = 0;
            // l is current group's first node
            // after this while, r point to (k+1)th node
            // which is next group's frist node 
            while(r && count < k){
                r = r->next;
                count++;
            }
            if(count == k){
                pre = r;
                cur = l;
                // 下面这个while把l到r之间的node反转。
                while(count--){
                    // 1 and 2 lines point cur->next to pre,
                    // 3 and 4 lines move pre and cur each by one node
                    ListNode *tmp = cur->next;
                    cur->next = pre;
                    pre = cur;
                    cur = tmp;
                }
                jump->next = pre;
                jump = l;   // l is right most node after reverse
                l = r;      // l point to next group's first node
            }else{
                // 剩下的不到k个
                return dummy_head->next;
            }
        }
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
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = jump = ListNode(0)
        dummy.next = l = r = head

        while True:
            count = 0
            while r and count < k:
                count += 1
                r = r.next
            if count == k:
                pre, cur = r, l
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