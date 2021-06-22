class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        while i * i < num:
            i += 1
        return i * i == num


def test(test_name, num, expected):
    res = Solution().isPerfectSquare(num)
    if type(res) == type(expected) and res == expected:
        print(test_name + ' succeed')
    else:
        print(test_name + ' fail')


if __name__ == '__main__':
    num1 = 16
    expected1 = True
    test('test1', num1, expected1)

    num2 = 14
    expected2 = False
    test('test2', num2, expected2)
