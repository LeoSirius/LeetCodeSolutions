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

def print_list(lst: ListNode):
    p = lst
    while p:
        print(p.val, end=', ')
        p = p.next