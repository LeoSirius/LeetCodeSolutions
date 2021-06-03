class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -(2 ** 31)

        is_neg = False
        if x < 0:
            is_neg = True
            x = -x

        res = 0
        while x:
            d = x % 10
            x //= 10
            if is_neg:
                if (res > INT_MAX // 10) or (res == INT_MAX // 10 and d > 8):
                    return 0
            else:
                if (res > INT_MAX // 10) or (res == INT_MAX // 10 and d > 7):
                    return 0
            res = res * 10 + d

        return -res if is_neg else res


def test(test_name, x, expected):
    res = Solution().reverse(x)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    test('test1', 123, 321)
    test('test2', -123, -321)
    test('test3', 120, 21)
    test('test4', 1534236469, 0)