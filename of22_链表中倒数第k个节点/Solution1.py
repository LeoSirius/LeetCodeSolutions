from util_py.list import *


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        fast, slow = head, head

        for _ in range(k):
            fast = fast.next
        
        while fast:
            fast = fast.next
            slow = slow.next
        
        return slow


def test(test_name, head, k, expected):
    res = Solution().getKthFromEnd(head, k)
    if is_equal_list(res, expected):
        print(f'{test_name} success.')
    else:
        print(f'{test_name} failed.')
    

if __name__ == "__main__":
    head1 = build_list([1,2,3,4,5])
    k1 = 2
    expected1 = build_list([4,5])
    test('test1', head1, k1, expected1)

    head2 = build_list([1])
    k2 = 1
    expected2 = build_list([1])
    test('test2', head2, k2, expected2)



# 输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，
# 即链表的尾节点是倒数第1个节点。例如，一个链表有6个节点，从头节点开始，
# 它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个节点是值为4的节点。

# 示例：

# 给定一个链表: 1->2->3->4->5, 和 k = 2.
# 返回链表 4->5.
