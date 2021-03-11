class Solution:
    def calculate(self, s: str) -> int:
        stk = []
        pre_op = '+'
        n = 0

        for i, ch in enumerate(s):
            if ch.isdigit():
                n = n * 10 + int(ch)
            if i == len(s) - 1 or ch in '+-*/':
                if pre_op == '+':
                    stk.append(n)
                elif pre_op == '-':
                    stk.append(-n)
                elif pre_op == '*':
                    stk.append(stk.pop() * n)
                elif pre_op == '/':
                    top = stk.pop()
                    if top < 0:
                        stk.append(int(top / n))
                    else:
                        stk.append(top // n)
                pre_op = ch
                n = 0
        return sum(stk)


def test(test_name, s, expected):
    res = Solution().calculate(s)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    s1 = "3+2*2"
    expected1 = 7
    test('test1', s1, expected1)

    s2 = " 3/2 "
    expected2 = 1
    test('test2', s2, expected2)

    s3 = " 3+5 / 2 "
    expected3 = 5
    test('test3', s3, expected3)


