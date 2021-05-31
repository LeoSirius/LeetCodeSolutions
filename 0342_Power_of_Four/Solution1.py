class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        x = 1
        while x < n:
            x *= 4
        return x == n


def test(test_name, n, expected):
    res = Solution().isPowerOfFour(n)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    n1 = 16
    expected1 = True
    test('test1', n1, expected1)

    n2 = 5
    expected2 = False
    test('test2', n2, expected2)

    n3 = 1
    expected3 = True
    test('test3', n3, expected3)
