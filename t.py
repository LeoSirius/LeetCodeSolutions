class Solution:
    def calculate(self, s: str) -> int:
        res, sign, n = 0, 1, 0
        stk = []

        for c in s:
            if c.isdigit():
                n = n * 10 + int(c)
            elif c in ['+', '-']:
                res += sign * n
                n = 0
                sign = 1 if c == '+' else -1
            elif c == '(':
                stk.append(res)
                stk.append(sign)
                res = 0
                sign = 1
            elif c == ')':
                res += sign * n
                n = 0
                res *= stk.pop()
                res += stk.pop()
        res += sign * n
        return res


def test(test_name, s, expected):
    res = Solution().calculate(s)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    s1 = "1 + 1"
    expected1 = 2
    test('test1', s1, expected1)

    s2 = " 2-1 + 2 "
    expected2 = 3
    test('test2', s2, expected2)

    s3 = "(1+(4+5+2)-3)+(6+8)"
    expected3 = 23
    test('test3', s3, expected3)

