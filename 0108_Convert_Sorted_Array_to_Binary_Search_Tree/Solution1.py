from typing import List

from utils_py.tree import *

class Solution:
    def build_tree(self, nums, start, end):
        # if start > end:
        #     return None
        # elif start == end:
        #     return TreeNode(nums[start])

        mid = start + (end - start) // 2
        # print("end - start = {}, (end - start) // 2 = {}, start + (end - start) // 2 = {}".format(
        #     end - start,
        #     (end - start) // 2,
        #     start + (end - start) // 2
        # ))
        node = TreeNode(nums[mid])
        if mid - start > 0:
            node.left = self.build_tree(nums, start, mid - 1)
        if end - mid > 0:
            node.right = self.build_tree(nums, mid + 1, end)
        return node

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        return self.build_tree(nums, 0, len(nums)-1)


def test(test_name, nums):
    # 这道题不要用is_same_tree来测试，答案不唯一
    res = Solution().sortedArrayToBST(nums)
    in_list = get_inorder_list(res)
    if in_list == nums:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    nums1 = [-10,-3,0,5,9]
    #       0
    #      / \
    #    -3   9
    #    /   /
    #  -10  5
    test('test1', nums1)
