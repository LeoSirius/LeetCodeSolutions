from typing import List

class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if not postorder or len(postorder) <= 2:
            return True
        node_val = postorder[-1]
        p = 0
        while p < len(postorder) and postorder[p] < node_val:
            p += 1
        for i in range(p, len(postorder)):
            if postorder[i] < node_val:
                return False

        return self.verifyPostorder(postorder[:p]) and self.verifyPostorder(postorder[p:-1])


def test(test_name, postorder, expected):
    res = Solution().verifyPostorder(postorder)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    postorder1 = [1,6,3,2,5]
    expected1 = False
    test('test1', postorder1, expected1)

    postorder2 = [1,3,2,6,5]
    expected2 = True
    test('test2', postorder2, expected2)


# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。
# 如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。
#
# 参考以下这颗二叉搜索树：
#
#      5
#     / \
#    2   6
#   / \
#  1   3
#
# 示例 1：
#
# 输入: [1,6,3,2,5]
# 输出: false
#
# 示例 2：
# 输入: [1,3,2,6,5]
# 输出: true
#  
#
# 提示：
# 数组长度 <= 1000
