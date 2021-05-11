from typing import *

class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        idx1, idx2 = -1, -1
        res = len(wordsDict)

        for i, w in enumerate(wordsDict):
            if w == word1:
                idx1 = i
            if w == word2:
                idx2 = i
            if idx1 != -1 and idx2 != -1:
                res = min(res, abs(idx1-idx2))
        return res


def test(test_name, wordsDict, word1, word2, expected):
    res = Solution().shortestDistance(wordsDict, word1, word2)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    wordsDict1 = ["practice", "makes", "perfect", "coding", "makes"]
    word11 = 'coding'
    word21 = 'practice'
    expected1 = 3
    test('test1', wordsDict1, word11, word21, expected1)

    wordsDict2 = ["practice", "makes", "perfect", "coding", "makes"]
    word12 = 'makes'
    word22 = 'coding'
    expected2 = 1
    test('test2', wordsDict2, word12, word22, expected2)
