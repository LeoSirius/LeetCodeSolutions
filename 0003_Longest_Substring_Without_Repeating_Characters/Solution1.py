from typing import *

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ch2idx = {}
        res, start = 0, 0
        for i, ch in enumerate(s):
            if ch in ch2idx:
                start = max(start, ch2idx[ch] + 1)
            ch2idx[ch] = i
            res = max(res, i - start + 1)
        return res


def test(test_name, s, expected):
    res = Solution().lengthOfLongestSubstring(s)
    print('res = {}'.format(res))
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    s1, expected1 = "abcabcbb", 3
    test('test1', s1, expected1)

    s2, expected2 = " ", 1
    test('test2', s2, expected2)

    s3 = "dvdf"
    expected3 = 3
    test('test3', s3, expected3)
