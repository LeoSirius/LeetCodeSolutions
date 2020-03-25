class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if not numerator:
            return '0'

        res = ''
        if not ((numerator > 0) == (denominator > 0)):
            res += '-'

        numerator, denominator = abs(numerator), abs(denominator)
        r = numerator % denominator
        res += str(numerator // denominator)
        if not r:
            return res
        
        res += '.'
        num2idx = {}
        while r:
            if r in num2idx.keys():
                res = res[:num2idx[r]] + '(' + res[num2idx[r]:]
                res += ')'
                break
            
            # 考虑4 / 333, 第一次进来的时候，
            # 三次循环后 {4: 2, 40: 3, 67: 4}， 我们再这里存r之后，res实际上增加了。所以多一个
            num2idx[r] = len(res)
            r *= 10
            res += str(r // denominator)
            r %= denominator
        return res

def test(test_name, numerator, denominator, expected):
    res = Solution().fractionToDecimal(numerator, denominator)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == "__main__":
    numerator1, denominator1 = 1, 2
    expected1 = "0.5"
    test('test1', numerator1, denominator1, expected1)

    numerator2, denominator2 = 2, 1
    expected2 = "2"
    test('test2', numerator2, denominator2, expected2)

    numerator3, denominator3 = 2, 3
    expected3 = "0.(6)"
    test('test3', numerator3, denominator3, expected3)

    numerator4, denominator4 = 0, 3
    expected4 = '0'
    test('test4', numerator4, denominator4, expected4)

    numerator5, denominator5 = -50, 8
    expected5 = '-6.25'
    test('test5', numerator5, denominator5, expected5)

    numerator6, denominator6 = 4, 333
    expected6 = '0.(012)'
    test('test6', numerator6, denominator6, expected6)
