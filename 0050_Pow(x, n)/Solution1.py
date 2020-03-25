class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not n:
            return 1
        if n < 0:
            x = 1 / x
            n = (-n)

        if n % 2 == 0:
            return self.myPow(x * x, n // 2)
        else:
            return self.myPow(x * x, n // 2) * x


def test(test_name, x, n, expected):
    res = Solution().myPow(x, n)
    print('res = {}'.format(res))
    if abs(res - expected) < 0.00001:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    x1 = 2.00000
    n1 = 10
    expected1 = 1024.00000
    test('test1', x1, n1, expected1)

    x2 = 2.10000
    n2 = 3
    expected2 = 9.26100
    test('test2', x2, n2, expected2)

    x3 = 2.00000
    n3 = -2
    expected3 = 0.25000
    test('test3', x3, n3, expected3)