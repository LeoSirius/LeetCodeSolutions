class Solution:
    def intToRoman(self, num: int) -> str:
        num_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        char_list = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

        i = 0
        res = ''
        while num:
            while num >= num_list[i]:
                num -= num_list[i]
                res += char_list[i]
            i += 1
        return res

def test(test_name, num, expected):
    res = Solution().intToRoman(num)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == "__main__":
    test('test1', 58, 'LVIII')
