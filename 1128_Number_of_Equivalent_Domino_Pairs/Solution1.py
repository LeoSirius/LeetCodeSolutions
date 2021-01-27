from typing import *
from collections import defaultdict

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        
        pair_dict = defaultdict(int)
        res = 0
        for pair in dominoes:
            pair = tuple(sorted(pair))
            pair_dict[pair] += 1

        for _, v in pair_dict.items():
            res += v * (v - 1) // 2
        return res


def test(test_name, dominoes, expected):
    res = Solution().numEquivDominoPairs(dominoes)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    dominoes1 = [[1,2],[2,1],[3,4],[5,6]]
    expected1 = 1
    test('test1', dominoes1, expected1)

    dominoes2 = [[1,2],[1,2],[1,1],[1,2],[2,2]]
    expected2 = 3
    test('test2', dominoes2, expected2)


# Given a list of dominoes, dominoes[i] = [a, b] is equivalent to 
# dominoes[j] = [c, d] if and only if either (a==c and b==d), 
# or (a==d and b==c) - that is, one domino can be rotated to be equal to 
# another domino.

# Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, 
# and dominoes[i] is equivalent to dominoes[j].

# Example 1:

# Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
# Output: 1
#  

# Constraints:

# 1 <= dominoes.length <= 40000
# 1 <= dominoes[i][j] <= 9
