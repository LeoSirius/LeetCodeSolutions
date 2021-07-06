from collections import defaultdict

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        lower, count = '', ''
        stk = [1]
        counter = defaultdict(int)
        for ch in reversed(formula):
            if ch.isdigit():
                count = ch + count
            elif ch.islower():
                lower = ch + lower
            elif ch == ')':
                stk.append(stk[-1] * int(count or '1'))
                count = ''
            elif ch == '(':
                stk.pop()
            elif ch.isupper():
                counter[ch + lower] += stk[-1] * int(count or '1')
                lower, count = '', ''

        res = ''
        for k, v in sorted(counter.items()):
            res += k
            res += str(v) if v > 1 else ''

        return res


def test(test_name, formula, expected):
    res = Solution().countOfAtoms(formula)
    if type(res) == type(expected) and res == expected:
        print(test_name + ' succeed')
    else:
        print(test_name + ' fail')


if __name__ == '__main__':
    formula1 = 'H2O'
    expected1 = 'H2O'
    test('test1', formula1, expected1)

    formula2 = 'Mg(OH)2'
    expected2 = 'H2MgO2'
    test('test2', formula2, expected2)

    formula3 = 'K4(ON(SO3)2)2'
    expected3 = 'K4N2O14S4'
    test('test3', formula3, expected3)

    formula4 = 'Be32'
    expected4 = 'Be32'
    test('test4', formula4, expected4)
