class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x < 1:
            x = 1 / x
        res = 1
        while res * res <= x:
            res += 1
        res -= 1
        return int(res)


def test(test_name, x, expected):
    res = Solution().mySqrt(x)
    if isinstance(res, int) and res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    x1, expected1 = 4, 2
    test("test1", x1, expected1)

    x2, expected2 = 8, 2
    test('test2', x2, expected2)

    x3, expected3 = 2, 1
    test('test3', x3, expected3)

    x4, expected4 = 4, 2
    test('test4', x4, expected4)

    x5, expected5 = 0, 0
    test('test5', x5, expected5)
