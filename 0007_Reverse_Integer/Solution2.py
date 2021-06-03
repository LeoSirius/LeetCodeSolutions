class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1

        # int() 会自动去掉字符串开头的0  int('001') = 1
        res = sign * int(str(sign * x)[::-1])

        if res > 2 ** 31 - 1 or res < -(2 ** 31):
            return 0
        return res


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
