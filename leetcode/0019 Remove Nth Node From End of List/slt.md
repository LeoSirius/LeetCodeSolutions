## 思路1 一块一慢法

fast是正数的n+1个元素，所以slow也是倒数的n+1个元素。所以最后是跳过slow的下一个元素，即第n个元素。

另外，注意处理n过多的情况。n >= len(list_name)的时候，都只用把第一个元素跳过即可，即返回head.next

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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *fast = head;
        ListNode *slow = head;
        while(n--){
            if(fast->next){
                fast = fast->next;
            }else{
                return head->next;
            }
        }
        while(fast->next){
            fast = fast->next;
            slow = slow->next;
        }
        slow->next = slow->next->next;
        return head;
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
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = slow = head
        for i in range(n):
            if fast.next:
                fast = fast.next
            else:
                # if fast.next does not exists, which means n >= length of linked list
                # so just remove the first node
                return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
```
