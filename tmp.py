class Solution:


    def trailingZeroes(self, n: int) -> int:
        res = 0
        i = 5
        while n // i:
            res += n // i
            i *= 5

        return res

def test(test_name, n, expected):
    res = Solution().trailingZeroes(n)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed')

if __name__ == "__main__":
    n1, expected1 = 3, 0
    test('test1', n1, expected1)

    n2, expected2 = 5, 1
    test('test2', n2, expected2)
