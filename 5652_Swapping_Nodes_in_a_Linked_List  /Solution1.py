from util_py.list import *


class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        fast, slow = head, head
        for _ in range(1,k):
            fast = fast.next

        tmp = fast
        while fast.next:     # fast最后指向最后一个，而不是最后一个的下一个。
            fast = fast.next
            slow = slow.next
        
        tmp.val, slow.val = slow.val, tmp.val
        return head


def test(test_name, head, k, expected):
    res = Solution().swapNodes(head, k)
    if is_equal_list(res, expected):
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    head1 = build_list([1,2,3,4,5])
    k1 = 2
    expected1 = build_list([1,4,3,2,5])
    test('test1', head1, k1, expected1)

    head2 = build_list([7,9,6,6,7,8,3,0,9,5])
    k2 = 5
    expected2 = build_list([7,9,6,6,8,7,3,0,9,5])
    test('test2', head2, k2, expected2)

    head3 = build_list([1])
    k3 = 1
    expected3 = build_list([1])
    test('test3', head3, k3, expected3)

    head4 = build_list([1,2])
    k4 = 1
    expecte4 = build_list([2,1])
    test('test4', head4, k4, expecte4)

    head5 = build_list([1,2,3])
    k5 = 2
    expecte5 = build_list([1,2,3])
    test('test5', head5, k5, expecte5)

