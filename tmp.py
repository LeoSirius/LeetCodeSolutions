class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:


def test(test_name, candidates, target, expected):
    res = Solution().combinationSum2(candidates, target, expected)
    [e.sort() for e in res]
    [e.sort() for e in expected]
    res.sort()
    expected.sort()
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name)


if __name__ == '__main__':



# Given a collection of candidate numbers (candidates) and 
# a target number (target), find all unique combinations 
# in candidates where the candidate numbers sums to target.

# Each number in candidates may only be used once in the combination.

# Note:

# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:

# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
# Example 2:

# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
#   [1,2,2],
#   [5]
# ]

