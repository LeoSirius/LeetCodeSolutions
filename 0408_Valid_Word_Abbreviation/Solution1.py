class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        _len, last = 0, 0

        for ch in abbr:
            if ch.isdigit():
                if last == 0 and ch == '0':
                    return False
                last = last * 10 + int(ch)
            else:
                # step1 加之前出现过的数字
                if last:
                    _len += last
                    last = 0
                # step2 加当前字母
                _len += 1

                if _len > len(word) or word[_len-1] != ch:
                    return False
        _len += last    # 最后一个是数组的情况

        return _len == len(word)


def test(test_name, word, abbr, expected):
    res = Solution().validWordAbbreviation(word, abbr)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    word1 = 'internationalization'
    abbr1 = 'i12iz4n'
    expected1 = True
    test('test1', word1, abbr1, expected1)

    word2 = 'apple'
    abbr2 = 'a2e'
    expected2 = False
    test('test2', word2, abbr2, expected2)
