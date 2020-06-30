from typing import *

class WordDistance:

    def __init__(self, words: List[str]):
        self.words = words
        mp = {}
        for i, v in enumerate(words):
            if v in mp:
                mp[v].append(i)
            else:
                mp[v] = [i]
        self.mp = mp

    def shortest(self, word1: str, word2: str) -> int:
        res = len(self.words)
        for i in self.mp[word1]:
            for j in self.mp[word2]:
                res = min(res, abs(i-j))
        return res


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)

def test(test_name: str, words, word1, word2, expected):
    obj = WordDistance(words)
    res = obj.shortest(word1, word2)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == "__main__":
    words1 = ["practice", "makes", "perfect", "coding", "makes"]
    word11 = 'coding'
    word21 = 'practice'
    expected1 = 3
    test('test1', words1, word11, word21, expected1)

    words2 = ["practice", "makes", "perfect", "coding", "makes"]
    word12 = 'makes'
    word22 = 'coding'
    expected2 = 1
    test('test2', words2, word12, word22, expected2)



# Design a class which receives a list of words in the constructor, 
# and implements a method that takes two words word1 and word2 and return 
# the shortest distance between these two words in the list. 
# Your method will be called repeatedly many times with different parameters. 

# Example:
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

# Input: word1 = “coding”, word2 = “practice”
# Output: 3

# Input: word1 = "makes", word2 = "coding"
# Output: 1

# Note:
# You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

