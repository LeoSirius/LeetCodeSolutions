class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for ch in columnTitle:
            res = res * 26 + ord(ch) - ord('A') + 1
        return res


def test(test_name, s, expected):
    res = Solution().titleToNumber(s)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    s1 = 'A'
    expected1 = 1
    test('test1', s1, expected1)

    s2 = 'AB'
    expected2 = 28
    test('test2', s2, expected2)

    s3 = 'ZY'
    expected3 = 701
    test('test3', s3, expected3)
