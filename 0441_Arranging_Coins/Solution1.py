class Solution:
    def arrangeCoins(self, n: int) -> int:
        row = 1
        remains = n
        while remains >= row:
            remains -= row
            row += 1
        return row-1


def test(test_name, n, expected):
    res = Solution().arrangeCoins(n)
    if type(res) == type(expected) and res == expected:
        print(test_name + ' succeed')
    else:
        print(test_name + ' fail')


if __name__ == '__main__':
    n1 = 5
    expected1 = 2
    test('test1', n1, expected1)

    n2 = 8
    expected2 = 3
    test('test2', n2, expected2)
