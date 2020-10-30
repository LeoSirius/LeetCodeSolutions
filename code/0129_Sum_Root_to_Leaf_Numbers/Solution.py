from util_py.tree import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        nums = []

        def dfs(node, curNum):
            if not node:
                return
            curNum = curNum * 10 + node.val
            if not node.left and not node.right:
                nums.append(curNum)
                return
            dfs(node.left, curNum)
            dfs(node.right, curNum)
        dfs(root, 0)
        return sum(nums)



def test(test_name, root, expected):
    res = Solution().sumNumbers(root)
    if res == expected:
        print(f'{test_name} success.')
    else:
        print(f'{test_name} failed.')


if __name__ == "__main__":
    #     1
    #    / \
    #   2   3
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    expected1 = 25
    test('test1', root1, expected1)

    #     4
    #    / \
    #   9   0
    #  / \
    # 5   1
    root2 = TreeNode(4)
    root2.left = TreeNode(9)
    root2.left.left = TreeNode(5)
    root2.left.right = TreeNode(1)
    root2.right = TreeNode(0)
    expected2 = 1026
    test('test2', root2, expected2)

    root3 = None
    expected3 = 0
    test('test3', root3, expected3)


# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

# An example is the root-to-leaf path 1->2->3 which represents the number 123.

# Find the total sum of all root-to-leaf numbers.

# Note: A leaf is a node with no children.

# Example:

# Input: [1,2,3]
#     1
#    / \
#   2   3
# Output: 25
# Explanation:
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Therefore, sum = 12 + 13 = 25.
# Example 2:

# Input: [4,9,0,5,1]
#     4
#    / \
#   9   0
#  / \
# 5   1
# Output: 1026
# Explanation:
# The root-to-leaf path 4->9->5 represents the number 495.
# The root-to-leaf path 4->9->1 represents the number 491.
# The root-to-leaf path 4->0 represents the number 40.
# Therefore, sum = 495 + 491 + 40 = 1026.
