# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def is_equal_list(l1: ListNode, l2: ListNode):
    if not l1 and not l2:
        return True
    if not l1 or not l2:
        return False
    if l1.val != l2.val:
        return False
    return is_equal_list(l1.next, l2.next)


def print_list_with_length(lst, length):
    p = lst
    while p and length:
        print(p.val, end=', ')
        p = p.next
        length -= 1


def print_list(lst: ListNode, length=0):
    p = lst
    if length:
        print_list(print_list_with_length(lst, length))
        return

    while p:
        print(p.val, end=', ')
        p = p.next


def build_list(arr):
    head = ListNode(0)
    p = head
    for n in arr:
        p.next = ListNode(n)
        p = p.next
    return head.next
