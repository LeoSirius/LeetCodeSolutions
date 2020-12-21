class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        dvd, dvs = abs(dividend), abs(divisor)
        res = 0

        while dvd >= dvs:
            x = 0
            # after this while     dvs << x <= dvd < dvs << (1 + x)
            while dvd >= (dvs << (1 + x)):
                x += 1
            res += 1 << x
            dvd -= dvs << x
        if not ((dividend > 0) == (divisor > 0)):
            res = -res
        
        return min(max(-(2 ** 31), res), 2 ** 31 - 1)

def test(test_name, dividend, divisor, expected):
    res = Solution().divide(dividend, divisor)
    print('res = {}'.format(res))
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    dividend1 = 10
    divisor1 = 3
    expected1 = 3
    test("test1", dividend1, divisor1, expected1)

    dividend2 = 7
    divisor2 = -3
    expected2 = -2
    test("test2", dividend2, divisor2, expected2)

    dividend3 = -1
    divisor3 = -1
    expected3 = 1
    test("test3", dividend3, divisor3, expected3)

    dividend4 = 2147483647
    divisor4 = 1
    expected4 = 2147483647
    test("test4", dividend4, divisor4, expected4)

    dividend5 = -2147483648
    divisor5 = -1
    expected5 = 2147483647
    test("test5", dividend5, divisor5, expected5)
