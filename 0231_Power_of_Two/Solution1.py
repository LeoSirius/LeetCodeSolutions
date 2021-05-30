class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        x = 1
        while x < n:
            x *= 2
        return x == n


def test(test_name, n, expected):
    res = Solution().isPowerOfTwo(n)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    n1 = 1
    expected1 = True
    test('test1', n1, expected1)

    n2 = 16
    expected2 = True
    test('test2', n2, expected2)

    n3 = 3
    expected3 = False
    test('test3', n3, expected3)

    n4 = 4
    expected4 = True
    test('test4', n4, expected4)

    n5 = 5
    expected5 = False
    test('test5', n5, expected5)

    n6 = 0
    expected6 = False
    test('test6', n6, expected6)
