from typing import *

class Solution:
    def getValidT9Words(self, num: str, words: List[str]) -> List[str]:
        ch2n = [2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9]

        candidates = []
        num = [int(n) for n in num]
        for word in words:
            idx = 0
            for ch in word:
                n = ch2n[ord(ch) - ord('a')]
                if n == num[idx]:
                    idx += 1
            if idx == len(num):
                candidates.append(word)

        return candidates


def test(test_name, num, words, expected):
    res = Solution().getValidT9Words(num, words)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    num1 = "8733"
    words1 = ["tree", "used"]
    expected1 = ["tree", "used"]
    test('test1', num1, words1, expected1)

    num2 = "2"
    words2 = ["a", "b", "c", "d"]
    expected2 = ["a", "b", "c"]
    test('test2', num2, words2, expected2)


# On old cell phones, users typed on a numeric keypad 
# and the phone would provide a list of words that matched 
# these numbers. Each digit mapped to a set of 0 - 4 letters. 
# Implement an algo­rithm to return a list of matching words, 
# given a sequence of digits. You are provided a list of valid 
# words. The mapping is shown in the diagram below:


# Example 1:

# Input: num = "8733", words = ["tree", "used"]
# Output: ["tree", "used"]

# Example 2:

# Input: num = "2", words = ["a", "b", "c", "d"]
# Output: ["a", "b", "c"]
# Note:

# num.length <= 1000
# words.length <= 500
# words[i].length == num.length
# There are no number 0 and 1 in num.

