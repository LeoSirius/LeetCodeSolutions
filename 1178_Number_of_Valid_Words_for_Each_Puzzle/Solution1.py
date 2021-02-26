from typing import *
import collections


class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        # set type is unhashable, so use frozenset
        counter = collections.Counter(frozenset(word) for word in words)
        res = []

        for puzzle in puzzles:
            # below three lines generate subsets of puzzle
            # see how this work at #0078
            subs = [puzzle[0]]
            for ch in puzzle[1:]:
                subs += [old_sub + ch for old_sub in subs]

            # for all subset of current puzzle's subsets
            #   get sum of count of subset which is in counter
            # in counter meanse that subset is in counter
            res.append(sum(counter[frozenset(s)] for s in subs))

        return res


def test(test_name, words, puzzles, expected):
    res = Solution().findNumOfValidWords(words, puzzles)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    words1 = ["aaaa","asas","able","ability","actt","actor","access"]
    puzzles1 = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
    expected1 = [1,1,3,2,4,0]
    test('test1', words1, puzzles1, expected1)

