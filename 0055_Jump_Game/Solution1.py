from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i, idx_reach = 0, 0
        while i <= idx_reach and i < len(nums):
            idx_reach = max(idx_reach, nums[i] + i)
            i += 1
        # 只有当i == len(nums)跳出时，返回true。即这时idx_reach仍然 >= i
        return i == len(nums)

def test(test_name, nums, expected):
    res = Solution().canJump(nums)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == "__main__":
    nums1 = [2,3,1,1,4]
    expected1 = True
    test('test1', nums1, expected1)

    nums2 = [3,2,1,0,4]
    expected2 = False
    test('test2', nums2, expected2)

    nums3 = [2,0,0]
    expected3 = True
    test('test3', nums3, expected3)
