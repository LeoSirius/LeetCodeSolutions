from typing import List
from utils_py.tree import *

class Solution:
    nums = []
    def build_tree(self, l, r):
        if l > r:
            return
        mid = l + ((r - l) >> 1)
        new_node = TreeNode(self.nums[mid])
        if l < mid:
            new_node.left = self.build_tree(l, mid - 1)
        if mid < r:
            new_node.right = self.build_tree(mid + 1, r)
        return new_node


    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not len(nums):
            return
        self.nums = nums
        return self.build_tree(0, len(nums) - 1)



def test(test_name, nums):
    # 这道题不要用is_equal_tree来测试，答案不唯一。但是他们的中序遍历的结果一定是唯一的
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
