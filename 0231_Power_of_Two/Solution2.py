class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n-1) == 0


def test(test_name, n, expected):
    res = Solution().isPowerOfTwo(n)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == "__main__":
    n1, expected1 = 1, True
    test('test1', n1, expected1)

    n2, expected2 = 16, True
    test('test2', n2, expected2)

    n3, expected3 = 218, False
    test('test3', n3, expected3)

    n4, expected4 = 0, False
    test('test4', n4, expected4)
