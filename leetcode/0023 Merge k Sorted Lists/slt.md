### 思路1 把所有节点放在一个list，再sort，再串起来

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

### 思路2 不断的两两merge

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
        if(lists.empty()){
            return nullptr;
        }
        while(lists.size() >= 2){
            lists.push_back(mergeTwoLists(lists[0], lists[1]));
            lists.erase(lists.begin());
            lists.erase(lists.begin());
        }
        return lists[0];
    }

    // 使用原来的结点merge，没有创建新的结点
    ListNode* mergeTwoLists(ListNode *l1, ListNode *l2){
        ListNode dummy_head = ListNode(0);
        ListNode *p = &dummy_head;
        while(l1 && l2){
            if(l1->val < l2->val){
                p->next = l1;
                l1 = l1->next;
            }else{
                p->next = l2;
                l2 = l2->next;
            }
            p = p->next;
        }
        if(l1){
            p->next = l1;
        }
        if(l2){
            p->next = l2;
        }
        return dummy_head.next;
    }
};
```