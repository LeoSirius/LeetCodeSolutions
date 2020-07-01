from utils_py.list import *

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
     	# 找个排头
        dummy = ListNode(-1)
        # pre = dummy
        # 依次拿head节点
        cur = head
        while cur:
        	# 把下一次节点保持下来
            pre = dummy
            tmp = cur.next
            # 找到插入的位置
            while pre.next and pre.next.val < cur.val:
                pre = pre.next
            # 进行插入操作
            cur.next = pre.next
            pre.next = cur

            # 移向下一个
            cur = tmp
        return dummy.next



def test(test_name, head, expected):
    res = Solution().insertionSortList(head)
    print_list(res)
    if is_equal_list(res, expected):
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == "__main__":
    head1 = ListNode(4)
    head1.next = ListNode(2)
    head1.next.next = ListNode(1)
    head1.next.next.next = ListNode(3)

    expected1 = ListNode(1)
    expected1.next = ListNode(2)
    expected1.next.next = ListNode(3)
    expected1.next.next.next = ListNode(4)

    test('test1', head1, expected1)

    head2 = ListNode(-1)
    head2.next = ListNode(5)
    head2.next.next = ListNode(3)
    head2.next.next.next = ListNode(4)
    head2.next.next.next.next = ListNode(0)

    expected2 = ListNode(-1)
    expected2.next = ListNode(0)
    expected2.next.next = ListNode(3)
    expected2.next.next.next = ListNode(4)
    expected2.next.next.next.next = ListNode(5)

    test('test2', head2, expected2)


# Algorithm of Insertion Sort:

# Insertion sort iterates, consuming one input element each repetition,
#  and growing a sorted output list.
# At each iteration, insertion sort removes one element from the input data,
#  finds the location it belongs within the sorted list, and inserts it there.
# It repeats until no input elements remain.

# Example 1:

# Input: 4->2->1->3
# Output: 1->2->3->4
# Example 2:

# Input: -1->5->3->4->0
# Output: -1->0->3->4->5

