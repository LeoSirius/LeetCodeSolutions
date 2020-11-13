from typing import *
from util_py.list import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        ohead, ehead = head, head.next
        p1, p2 = ohead, ehead

        while p2 and p2.next:
            p1.next = p1.next.next
            p2.next = p2.next.next
            p1 = p1.next
            p2 = p2.next

        p1.next = ehead
        return ohead


def test(test_name, head, expected):
    res = Solution().oddEvenList(head)
    if is_equal_list(res, expected):
        print(f'{test_name} success.')
    else:
        print(f'{test_name} failed.')


if __name__ == "__main__":
    head1 = build_list([1,2,3,4,5])
    expected1 = build_list([1,3,5,2,4])
    test('test1', head1, expected1)

    head2 = build_list([2,1,3,5,6,4,7])
    expected2 = build_list([2,3,6,7,1,5,4])
    test('test2', head2, expected2)


# Given a singly linked list, group all odd nodes together 
# followed by the even nodes. Please note here we are talking
#  about the node number and not the value in the nodes.

# You should try to do it in place. The program should run in O(1)
#  space complexity and O(nodes) time complexity.

# Example 1:

# Input: 1->2->3->4->5->NULL
# Output: 1->3->5->2->4->NULL
# Example 2:

# Input: 2->1->3->5->6->4->7->NULL
# Output: 2->3->6->7->1->5->4->NULL
#  

# Constraints:

# The relative order inside both the even and odd groups 
# should remain as it was in the input.
# The first node is considered odd, the second node even and so on ...
# The length of the linked list is between [0, 10^4].

