class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, h = 0, int(c ** 0.5)
        while l <= h:
            _sum = l * l + h * h
            if _sum < c:
                l += 1
            elif _sum > c:
                h -= 1
            else:
                return True

        return False


def test(test_name, c, expected):
    res = Solution().judgeSquareSum(c)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    c1 = 5
    expected1 = True
    test('test1', c1, expected1)

    c2 = 3
    expected2 = False
    test('test2', c2, expected2)

    c3 = 4
    expected3 = True
    test('test3', c3, expected3)

    c4 = 2
    expected4 = True
    test('test4', c4, expected4)

    c5 = 1
    expected5 = True
    test('test5', c5, expected5)
