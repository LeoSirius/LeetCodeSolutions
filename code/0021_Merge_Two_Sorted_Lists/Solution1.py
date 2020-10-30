from utils_py.list import *

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        p = dummy
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        p.next = l1 if l1 else l2
        return dummy.next



def test(test_name, l1, l2, expected):
    res = Solution().mergeTwoLists(l1, l2)
    if is_equal_list(res, expected):
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    l11 = ListNode(1)
    l11.next = ListNode(2)
    l11.next.next = ListNode(4)

    l21 = ListNode(1)
    l21.next = ListNode(3)
    l21.next.next = ListNode(4)

    expected1 = ListNode(1)
    expected1.next = ListNode(1)
    expected1.next.next = ListNode(2)
    expected1.next.next.next = ListNode(3)
    expected1.next.next.next.next = ListNode(4)
    expected1.next.next.next.next.next = ListNode(4)

    # 输入：1->2->4, 1->3->4
    # 输出：1->1->2->3->4->4
    test("test1", l11, l21, expected1)


# 输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。
#
# 示例1：
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
#
# 限制：
# 0 <= 链表长度 <= 1000
