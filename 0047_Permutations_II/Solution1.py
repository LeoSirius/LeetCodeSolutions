from typing import *


class Solution:

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        def dfs(nums, size, depth, path, used, res):
            if depth == size:
                res.append(path.copy())
                return
            for i in range(size):
                if used[i]:
                    continue

                if 0 < i and nums[i] == nums[i-1] and not used[i-1]:
                    continue

                used[i] = True
                path.append(nums[i])
                dfs(nums, size, depth + 1, path, used, res)
                used[i] = False
                path.pop()

        size = len(nums)
        if size == 0:
            return []

        nums.sort()

        used = [False] * len(nums)  # used进行剪枝
        res = []
        dfs(nums, size, 0, [], used, res)
        return res


def test(test_name, nums, expected):
    res = Solution().permuteUnique(nums)
    res.sort()
    expected.sort()
    print(res)
    print(expected)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    nums1 = [1,1,2];
    expected1 = [
        [1,1,2],
        [1,2,1],
        [2,1,1],
    ];
    test("test1", nums1, expected1);

    nums2 = [3,3,0,3];
    expected2 = [
        [0,3,3,3],
        [3,0,3,3],
        [3,3,0,3],
        [3,3,3,0]
    ];
    test("test2", nums2, expected2);

    nums3 = [2,2,1,1]
    expected3 = [
        [1,1,2,2],
        [1,2,1,2],
        [1,2,2,1],
        [2,1,1,2],
        [2,1,2,1],
        [2,2,1,1]
    ]
    test('test3', nums3, expected3)


# Given a collection of numbers that might contain duplicates, 
# return all possible unique permutations.

# Example:

# Input: [1,1,2]
# Output:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]
