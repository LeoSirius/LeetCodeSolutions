from typing import *

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        size = len(nums)

        def dfs(start, path):
            if start == size - 1:
                res.append(path)
                return

            for i in range(start, size):
                if start < i and nums[start] == nums[i]:
                    continue
                path[i], path[start] = path[start], path[i]
                dfs(start + 1, path[:])
                # path[i], path[start] = path[start], path[i]

        dfs(0, nums)
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
    # test("test1", nums1, expected1);

    nums2 = [3,3,0,3];
    expected2 = [
        [0,3,3,3],
        [3,0,3,3],
        [3,3,0,3],
        [3,3,3,0]
    ];
    # test("test2", nums2, expected2);

    nums3 = [2,2,1,1]
    expected3 = [
        [1,1,2,2],
        [1,2,1,2],
        [1,2,2,1],
        [2,1,1,2],
        [2,1,2,1],
        [2,2,1,1]
    ]
    # [[1,1,2,2],[1,2,1,2],[1,2,2,1],[2,1,1,2],[2,1,2,1],[2,2,1,1]]
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

