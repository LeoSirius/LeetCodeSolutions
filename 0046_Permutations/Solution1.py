from typing import *

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        size = len(nums)

        def dfs(start, path):
            if start == size:
                res.append(path)
                return

            for i in range(start, size):
                path[i], path[start] = path[start], path[i]
                dfs(start + 1, path[:])
                path[i], path[start] = path[start], path[i]
        
        dfs(0, nums)
        return res


def test(test_name, nums, expected):
    res = Solution().permute(nums)
    if res.sort() == expected.sort():
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    nums1 = [1,2,3];
    expected1 = [
        [1,2,3],
        [1,3,2],
        [2,1,3],
        [2,3,1],
        [3,2,1],
        [3,1,2],
    ];
    test("test1", nums1, expected1);


# Given a collection of distinct integers, return all possible permutations.

# Example:

# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
