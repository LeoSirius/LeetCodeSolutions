from utils_py.list import *

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return

        small, big, equal = None, None, None
        cur = head
        # 这里用头插法，把链表分成三段，head作为轴
        while cur:
            tmp = cur
            cur = cur.next
            if tmp.val < head.val:
                tmp.next = small
                small = tmp
            elif tmp.val > head.val:
                tmp.next = big
                big = tmp
            else:
                tmp.next = equal
                equal = tmp
        
        big = self.sortList(big)
        small = self.sortList(small)

        dummy = ListNode(0)
        p = dummy

        # 把小中大三段串起来
        for cur in [small, equal, big]:
            while cur:
                p.next = cur
                p = p.next
                cur = cur.next
                p.next = None
        return dummy.next


def test(test_name, head, expected):
    res = Solution().sortList(head)
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
