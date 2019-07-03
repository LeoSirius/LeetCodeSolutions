### 思路1 把所有节点放在一个list，再sort，再串起来

`python`的`sorted`可以制定排序对象的比较成员。`sorted(sorted_list, key=operator.attrgetter('val'))`就是用每个元素的`val`成员来进行排序。

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

        # 排好序，然后把他们串起来
        all_nodes = sorted(all_nodes, key=operator.attrgetter('val'))
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