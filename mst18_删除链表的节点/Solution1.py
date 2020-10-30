from util_py.list import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        pre_head = ListNode(0)
        pre_head.next = head
        p = pre_head

        while p.next:
            if p.next.val == val:
                p.next = p.next.next
                break
            p = p.next
        return pre_head.next


def test(test_name, head, val, expected):
    res = Solution().deleteNode(head, val)
    if is_equal_list(res, expected):
        print(f'{test_name} success.')
    else:
        print(f'{test_name} failed.')


if __name__ == "__main__":
    head1 = build_list([4,5,1,9])
    val1 = 5
    expected1 = build_list([4,1,9])
    test('test1', head1, val1, expected1)

    head2 = build_list([4,5,1,9])
    val2 = 1
    expected2 = build_list([4,5,9])
    test('test2', head2, val2, expected2)


# 给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。

# 返回删除后的链表的头节点。

# 注意：此题对比原题有改动

# 说明：

# 题目保证链表中节点的值互不相同
# 若使用 C 或 C++ 语言，你不需要 free 或 delete 被删除的节点


# 示例 1:

# 输入: head = [4,5,1,9], val = 5
# 输出: [4,1,9]
# 解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.


# 示例 2:

# 输入: head = [4,5,1,9], val = 1
# 输出: [4,5,9]
# 解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
#  

# 说明：

# 题目保证链表中节点的值互不相同
# 若使用 C 或 C++ 语言，你不需要 free 或 delete 被删除的节点

