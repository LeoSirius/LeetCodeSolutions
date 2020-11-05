from typing import *


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        que = [beginWord]
        word_len = len(beginWord)
        res = 0

        while len(que):
            res += 1
            cur_border_size = len(que)
            for _ in range(cur_border_size):
                cur_word = que.pop(0)
                if cur_word == endWord:
                    return res

                # python for loop中改变元素，必须这样
                for i in range(len(wordList)):
                    if wordList[i] == '':
                        continue
                    diff_cnt = 0
                    for j in range(word_len):
                        if cur_word[j] != wordList[i][j]:
                            diff_cnt += 1
                        if diff_cnt > 1:
                            break
                    if diff_cnt == 1:
                        que.append(wordList[i])
                        wordList[i] = ''
        return 0


def test(test_name, beginWord, endWord, wordList, expected):
    res = Solution().ladderLength(beginWord, endWord, wordList)
    if res == expected:
        print(f'{test_name} success.')
    else:
        print(f'{test_name} failed.')


if __name__ == "__main__":
    beginWord1 = 'hit'
    endWord1 = 'cog'
    wordList1 = ["hot","dot","dog","lot","log","cog"]
    expected1 = 5
    test('test1', beginWord1, endWord1, wordList1, expected1)

    beginWord2 = 'hit'
    endWord2 = 'cog'
    wordList2 = ["hot","dot","dog","lot","log"]
    expected2 = 0
    test('test2', beginWord2, endWord2, wordList2, expected2)


# Given two words (beginWord and endWord), and a dictionary's' word list,
#  find the length of shortest transformation sequence from beginWord to endWord,
#  such that:

# Only one letter can be changed at a time.
# Each transformed word must exist in the word list.
# Note:

# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.

# Example 1:

# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]

# Output: 5

# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.

# Example 2:

# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]

# Output: 0

# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

