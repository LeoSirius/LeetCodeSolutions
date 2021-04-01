class Solution:
    def clumsy(self, N: int) -> int:
        stk = [N]
        op = 0
        for i in range(N-1, 0, -1):
            if op == 0:
                stk.append(stk.pop() * i)
            elif op == 1:
                stk.append(int(stk.pop() / float(i)))
            elif op == 2:
                stk.append(i)
            elif op == 3:
                stk.append(-i)
            op = (op + 1) % 4
        return sum(stk)


def test(test_name, N, expected):
    res = Solution().clumsy(N)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    N1 = 4
    expected1 = 7
    test('test1', N1, expected1)

    N2 = 10
    expected2 = 12
    test('test2', N2, expected2)

    N3 = 7
    expected3 = 6
    test('test3', N3, expected3)
