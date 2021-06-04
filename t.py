from util_py.list import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p1, p2 = headA, headB
        while p1 != p2:
            # 最后一个 None 要走到，不然没有intersection的时候跳不出去
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA
        return p1


def test(test_name, headA: ListNode, headB: ListNode, expected: ListNode):
    res = Solution().getIntersectionNode(headA, headB)
    if is_equal_list(res, expected):
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    # 输入：intersectVal = 8,
    # listA = [4,1,8,4,5],
    # listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
    # 输出：Reference of the node with value = 8
    headA1 = build_list([4,1,8,4,5])
    headB1 = build_list([5,0,1])
    headB1.next.next.next = headA1.next.next
    expected1 = build_list([8,4,5])

    test('test1', headA1, headB1, expected1)

    headA2 = build_list([2,6,4])
    headB2 = build_list([1,5])
    expected2 = None
    test('test2', headA2, headB2, expected2)
