

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        p = head
        while p:
            node = Node(p.val, p.next, None)
            p.next = node
            p = node.next

        p = head
        while p:
            if p.random:
                p.next.random = p.random.next
            p = p.next.next

        res, p = head.next, head
        while p.next:
            # 在cpp中需要用一个tmp来保存next.next节点，python中一行就行。注意顺序不能变
            p.next, p = p.next.next, p.next

        return res

def test(test_name, head):
    # 这道题暂时测输入和输出两个链表的节点的数值顺序
    res = Solution().copyRandomList(head)
    input_list, output_list = [], []

    p = head
    while p:
        input_list.append(p.val)
        p = p.next
    p = res
    while p:
        output_list.append(p.val)
        p = p.next

    if input_list == output_list:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')
    
    
if __name__ == '__main__':
    # 7 -> 13 -> 11 -> 10 -> 1
    # random
    # 31 -> 7
    # 11 -> 1
    # 10 -> 11
    # 1 -> 7
    a0 = Node(7)
    a1 = Node(13)
    a2 = Node(11)
    a3 = Node(10)
    a4 = Node(1)
    a0.next = a1 
    a1.next = a2 
    a2.next = a3 
    a3.next = a4
    a1.random = a0
    a2.random = a4
    a3.random = a2
    a4.random = a0
    test("test1", a0)