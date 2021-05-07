class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = 0
        for i in range(0, n):
            current = start + 2 * i
            res ^= current
        return res


def test(test_name, n, start, expected):
    res = Solution().xorOperation(n, start)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    n1 = 5
    start1 = 0
    expected1 = 8
    test('test1', n1, start1, expected1)

    n2 = 4
    start2 = 3
    expected2 = 8
    test('test2', n2, start2, expected2)

    n3 = 1
    start3 = 7
    expected3 = 7
    test('test3', n3, start3, expected3)

    n4 = 10
    start4 = 5
    expected4 = 2
    test('test4', n4, start4, expected4)
