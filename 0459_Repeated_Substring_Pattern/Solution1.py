class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s+s)[1:-1]


def test(test_name, s, expected):
    res = Solution().repeatedSubstringPattern(s)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    s1 = 'abab'
    expected1 = True
    test('test1', s1, expected1)

    s2 = 'aba'
    expected2 = False
    test('test2', s2, expected2)

    s3 = 'abcabcabcabc'
    expected3 = True
    test('test3', s3, expected3)

