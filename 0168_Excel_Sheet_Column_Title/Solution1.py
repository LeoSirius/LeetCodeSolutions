class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber > 0:
            columnNumber -= 1
            columnNumber, m = divmod(columnNumber, 26)
            res.append(chr(ord('A') + m))
        return ''.join(reversed(res))


def test(test_name, n, expected):
    res = Solution().convertToTitle(n)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    n1 = 1
    expected1 = 'A'
    test('test1', n1, expected1)

    n2 = 28
    expected2 = 'AB'
    test('test2', n2, expected2)

    n3 = 701
    expected3 = 'ZY'
    test('test3', n3, expected3)
