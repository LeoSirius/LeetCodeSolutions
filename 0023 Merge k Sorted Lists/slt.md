### 思路1 不断的两两merge

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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        ListNode *res = nullptr;
        if (lists.size() == 0) {
            return res;
        } else if (lists.size() == 1) {
            return lists[0];
        }
        while (lists.size() > 1) {
            res = mergeTwo(lists[0], lists[1]);
            lists.erase(lists.begin(), lists.begin()+2);  // vector.erase 很慢
            lists.push_back(res);
        }
        return res;
    }

    ListNode* mergeTwo(ListNode *h1, ListNode *h2)
    {
        ListNode head(0);
        ListNode *l1, *l2, *p;
        p = &head;
        l1 = h1; l2 = h2;
        int v1, v2;
        while (l1 || l2) {
            v1 = l1 ? l1->val : __INT_MAX__;
            v2 = l2 ? l2->val : __INT_MAX__;
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

### 思路2 把所有节点放在一个list，再sort，再串起来

`python`的`sorted`可以制定排序对象的比较成员。`sorted(sorted_list, key=operator.attrgetter('val'))`就是用每个元素的`val`成员来进行排序。或者可以直接用lambda表达式。

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        all_nodes = []

        # 先把所有结点放到 all_nodes 中
        for head in lists:
            curr = head
            while curr is not None:
                all_nodes.append(curr)
                curr = curr.next

        # 排好序，然后把他们串起来, key = val 按照元素的val排序
        all_nodes = sorted(all_nodes, key=lambda: e: e.val)
        for i, node in enumerate(all_nodes):
            try:
                node.next = all_nodes[i + 1]  # 每个结点的next指向下一个结点
            except:
                node.next = None        # 最后一个结点

        # 注意是返回头结点
        if all_nodes:
            return all_nodes[0]
        else:
            return None
```
