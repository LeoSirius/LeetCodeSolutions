from typing import *
from collections import defaultdict, Counter
from heapq import *

class Word:
    def __init__(self, word: str, fre: int):
        self.word = word
        self.fre = fre

    def __lt__(self, other):
        if self.fre != other.fre:
            return self.fre < other.fre
        return self.word > other.word


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        hp = []
        heapify(hp)

        for w, fre in counter.items():
            heappush(hp, Word(w, fre))
            if len(hp) > k:
                heappop(hp)

        hp.sort(reverse=True)
        return [w.word for w in hp]


def test(test_name, words, k, expected):
    res = Solution().topKFrequent(words, k)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    words1 = ["i", "love", "leetcode", "i", "love", "coding"]
    k1 = 2
    expected1 = ["i", "love"]
    test('test1', words1, k1, expected1)

    words2 = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
    k2 = 4
    expected2 = ["the", "is", "sunny", "day"]
    test('test2', words2, k2, expected2)
