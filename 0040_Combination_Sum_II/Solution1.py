from typing import List

class Solution:
    def dfs(self, nums, target, start, path, res):
        if target < 0:
            return
        if target == 0:
            res.append(path)
            return
        
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            self.dfs(nums, target-nums[i], i+1, path+[nums[i]], res)

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()
        self.dfs(candidates, target, 0, path, res)
        return res


def test(test_name, candidates, target, expected):
    res = Solution().combinationSum2(candidates, target)
    [e.sort() for e in res]
    [e.sort() for e in expected]
    res.sort()
    expected.sort()
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':

    candidates1 = [10, 1, 2, 7, 6, 1, 5]
    target1 = 8
    expected1 = [
        [1, 7],
        [1, 2, 5],
        [2, 6],
        [1, 1, 6]
    ]
    test('test1', candidates1, target1, expected1)

    candidates2 = [2,5,2,1,2]
    target2 = 5
    expected2 = [
        [1,2,2],
        [5]
    ]
    test('test2', candidates2, target2, expected2)

    candidates3 = [3,1,3,5,1,1]
    target3 = 8
    expected3 = [[1,1,1,5],[1,1,3,3],[3,5]]
    test('test3', candidates3, target3, expected3)
