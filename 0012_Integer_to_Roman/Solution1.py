class Solution:
    def intToRoman(self, num: int) -> str:
        I = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        X = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        C = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        M = ['', 'M', 'MM', 'MMM']
        return M[num//1000] + C[num//100%10] + X[num//10%10] + I[num%10]


def test(test_name, num, expected):
    res = Solution().intToRoman(num)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    test('test1', 58, 'LVIII')
