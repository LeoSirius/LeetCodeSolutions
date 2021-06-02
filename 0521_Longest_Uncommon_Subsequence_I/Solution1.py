class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1
        la, lb = len(a), len(b)
        return max(la, lb)


def test(test_name, a, b, expected):
    res = Solution().findLUSlength(a, b)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    a1 = 'aba'
    b1 = 'cdc'
    expected1 = 3
    test('test1', a1, b1, expected1)

    a2 = 'aaa'
    b2 = 'bbb'
    expected2 = 3
    test('test2', a2, b2, expected2)

    a3 = 'aaa'
    b3 = 'aaa'
    expected3 = -1
    test('test3', a3, b3, expected3)
