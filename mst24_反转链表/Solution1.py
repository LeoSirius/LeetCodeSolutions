from util_py.list import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        pre, cur = None, head
        while cur:
            tmp = cur.next
            cur.next = pre

            pre, cur = cur, tmp
        return pre


def test(test_name, head, expected):
    res = Solution().reverseList(head)
    print_list(res)
    if is_equal_list(res, expected):
        print(f'{test_name} success.')
    else:
        print(f'{test_name} failed.')


if __name__ == "__main__":
    head1 = build_list([1,2,3,4,5])
    expected1 = build_list([5,4,3,2,1])
    test('test1', head1, expected1)

    head2 = build_list([])
    expected2 = build_list([])
    test('test2', head2, expected2)


# 定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

# 示例:
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
#  

# 限制：
# 0 <= 节点个数 <= 5000

