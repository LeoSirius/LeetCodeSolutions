class Solution:
    def addDigits(self, num: int) -> int:
        def process(n):
            res = 0
            while n:
                res += n % 10
                n //= 10
            return res

        while num >= 10:
            num = process(num)
        return num


def test(test_name, num, expected):
    res = Solution().addDigits(num)
    if res == expected:
        print(test_name + ' succeed')
    else:
        print(test_name + ' fail')


if __name__ == '__main__':
    num1 = 38
    expected1 = 2
    test('test1', num1, expected1)

    num2 = 0
    expected2 = 0
    test('test2', num2, expected2)

    num3 = 10
    expected3 = 1
    test('test3', num3, expected3)
