class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1


def test(test_name, n, expected):
    res = Solution().isPowerOfThree(n)
    if type(res) == type(expected) and res == expected:
        print(test_name + ' succeed')
    else:
        print(test_name + ' fail')


if __name__ == '__main__':
    n1 = 27
    expected1 = True
    test('test1', n1, expected1)

    n2 = 0
    expected2 = False
    test('test2', n2, expected2)

    n3 = 9
    expected3 = True
    test('test3', n3, expected3)

    n4 = 45
    expected4 = False
    test('test4', n4, expected4)
