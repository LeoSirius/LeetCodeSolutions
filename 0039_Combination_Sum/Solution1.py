from typing import *

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        size = len(candidates)
        res = []

        def dfs(target, start, path):
            if target < 0:
                return
            elif target == 0:
                res.append(path)
                return
            
            for i in range(start, size):
                dfs(target-candidates[i], i, path + [candidates[i]])
        
        dfs(target, 0, [])
        return res


def test(test_name, candidates, target, expected):
    res = Solution().combinationSum(candidates, target)
    [item.sort() for item in res]
    [item.sort() for item in expected]
    res.sort()
    expected.sort()
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    nums1 = [2,3,6,7]
    target1 = 7
    expected1 = [
        [7], [2,2,3]
    ]
    test('test1', nums1, target1, expected1)

    nums2 = [2,3,5]
    target2 = 8
    expected2 = [
        [2,2,2,2],
        [2,3,3],
        [3,5]
    ]
    test('test2', nums2, target2, expected2)
