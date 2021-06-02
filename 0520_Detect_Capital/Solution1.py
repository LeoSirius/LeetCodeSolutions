class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        _len = len(word)
        if _len <= 1:
            return True

        up_cnt, lo_cnt = 0, 0
        for ch in word:
            if ch.isupper():
                up_cnt += 1
            else:
                lo_cnt += 1
        if (up_cnt == _len or
                lo_cnt == _len or
                word[0].isupper() and lo_cnt == _len - 1):
            return True
        return False


def test(test_name, word, expected):
    res = Solution().detectCapitalUse(word)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    word1 = 'USA'
    expected1 = True
    test('test1', word1, expected1)

    word2 = 'FlaG'
    expected2 = False
    test('test2', word2, expected2)

    word3 = 'FFFFFFFFFFFFFFFFFFFFf'
    expected3 = False
    test('test3', word3, expected3)

    word4 = 'ffffffffffffffffffffF'
    expected4 = False
    test('test4', word4, expected4)

    word5 = 'Leetcode'
    expected5 = True
    test('test5', word5, expected5)

