
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode(0)
        p = dummy_head
        carry = 0

        while l1 or l2 or carry:
            v1, v2 = 0, 0

            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next

            carry, val = divmod(v1 + v2 + carry, 10)
            p.next = ListNode(val)
            p = p.next
        
        return dummy_head.next

def is_same(l1, l2):
    p1, p2 = l1, l2
    while p1 and p2:
        if p1.val != p2.val:
            return False
        p1, p2 = p1.next, p2.next
    
    return p1 == None and p2 == None

def test(test_name, l1, l2, expected):
    res = Solution().addTwoNumbers(l1, l2)
    if is_same(res, expected):
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')



if __name__ == "__main__":
    l11 = ListNode(2)
    l11.next = ListNode(4)
    l11.next.next = ListNode(3)

    l21 = ListNode(5)
    l21.next = ListNode(6)
    l21.next.next = ListNode(4)

    expected1 = ListNode(7)
    expected1.next = ListNode(0)
    expected1.next.next = ListNode(8)

    test('test1', l11, l21, expected1)

    l12 = ListNode(5)
    l22 = ListNode(5)

    expected2 = ListNode(0)
    expected2.next = ListNode(1)
    test('test2', l12, l22, expected2)
