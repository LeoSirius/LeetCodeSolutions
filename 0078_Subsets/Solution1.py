from typing import *

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(path, start):
            res.append(path)
            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(path[:], i + 1)
                path.pop()
        
        dfs([], 0)
        return res

def test(test_name, nums, expected):
    res = Solution().subsets(nums)
    print(res)
    if sorted(res) == sorted(expected):
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == "__main__":
    nums1 = [1,2,3]
    expected1 = [
        [3],
        [1],
        [2],
        [1,2,3],
        [1,3],
        [2,3],
        [1,2],
        []
    ]
    test('test1', nums1, expected1)


# Given a set of distinct integers, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.

# Example:

# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
