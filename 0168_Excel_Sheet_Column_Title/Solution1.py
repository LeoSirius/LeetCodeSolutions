class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ''

        while n:
            n -= 1  # n start from 1, so -1.  先在这里减1，能避免很多corner cases
            n, r = divmod(n, 26)   # 0 <= r <= 25
            res = chr(r + ord('A')) + res

        return res

def test(test_name, n, expected):
    res = Solution().convertToTitle(n)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == "__main__":
    n1 = 1
    expected1 = 'A'
    test('test1', n1, expected1)

    n2 = 28
    expected2 = 'AB'
    test('test2', n2, expected2)

    n3 = 701
    expected3 = 'ZY'
    test('test3', n3, expected3)
