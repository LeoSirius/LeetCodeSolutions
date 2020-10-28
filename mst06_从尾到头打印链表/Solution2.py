from typing import *

from util_py.list import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        res = []

        def recurse(node):
            if not node:
                return
            recurse(node.next)
            res.append(node.val)
        recurse(head)
        return res


def test(test_name, head, expected):
    res = Solution().reversePrint(head)
    if res == expected:
        print(f'{test_name} success.')
    else:
        print(f'{test_name} failed.')


if __name__ == "__main__":
    head1 = build_list([1,3,2])
    expected1 = [2,3,1]
    test('test1', head1, expected1)



# 输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

# 示例 1：

# 输入：head = [1,3,2]
# 输出：[2,3,1]