class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 2 == 0:
            n //= 2
        while n % 3 == 0:
            n //= 3
        while n % 5 == 0:
            n //= 5
        return n == 1


def test(test_name, n, expected):
    res = Solution().isUgly(n)
    if type(res) == type(expected) and res == expected:
        print(test_name + ' succeed')
    else:
        print(test_name + ' fail')


if __name__ == '__main__':
    n1 = 6
    expected1 = True
    test('test1', n1, expected1)

    n2 = 8
    expected2 = True
    test('test2', n2, expected2)

    n3 = 14
    expected3 = False
    test('test3', n3, expected3)

    n4 = 1
    expected4 = True
    test('test4', n4, expected4)