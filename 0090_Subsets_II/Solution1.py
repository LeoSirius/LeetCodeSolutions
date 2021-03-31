from typing import *

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        def dfs(start, subset):
            subsets.append(subset)
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                subset.append(nums[i])
                dfs(i+1, subset[:])
                subset.pop()

        nums.sort()
        dfs(0, [])
        return subsets


def test(test_name, nums, expected):
    res = Solution().subsetsWithDup(nums)
    [item.sort() for item in res]
    res.sort()
    [item.sort() for item in expected]
    expected.sort()
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    nums1 = [1,2,2]
    expected1 = [[],[1],[1,2],[1,2,2],[2],[2,2]]
    test('test1', nums1, expected1)

    nums2 = [0]
    expected2 = [[], [0]]
    test('test2', nums2, expected2)

    nums3 = [4,4,4,1,4]
    expected3 = [[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]
    test('test3', nums3, expected3)
