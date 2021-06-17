class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if ' ' in s:
            return False

        def check(s, need_integer=False):
            dot_count, digit_count = 0, 0
            for i, ch in enumerate(s):
                if ch not in ['-', '+', '.'] and not ch.isdigit():
                    return False

                if ch == '.':
                    if need_integer:
                        return False
                    dot_count += 1
                if ch.isdigit():
                    digit_count += 1
                if i > 0 and ch in ['-', '+']:
                    return False
            if dot_count > 1 or digit_count < 1:
                return False
            return True

        if 'e' in s or 'E' in s:
            splited = s.split('e') if 'e' in s else s.split('E')
            if len(splited) != 2:
                return False
            return check(splited[0]) and check(splited[1], need_integer=True)
        return check(s)


def test(test_name, s, expected):
    res = Solution().isNumber(s)
    if type(res) == type(expected) and res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    s1 = '0'
    expected1 = True
    test('test1', s1, expected1)

    s2 = ' 0.1'
    expected2 = True
    test('test2', s2, expected2)

    s3 = 'abc'
    expected3 = False
    test('test3', s3, expected3)

    s4 = '1 a'
    expected4 = False
    test('test4', s4, expected4)

    s5 = '2e10'
    expected5 = True
    test('test5', s5, expected5)

    s6 = ' -90e3'
    expected6 = True
    test('test6', s6, expected6)

    s7 = ' 1e'
    expected7 = False
    test('test7', s7, expected7)

    s8 = 'e3'
    expected8 = False
    test('test8', s8, expected8)

    s9 = '6e-1'
    expected9 = True
    test('test9', s9, expected9)

    s10 = ' 99e2.5 '
    expected10 = False
    test('test10', s10, expected10)

    s11 = '53.5e93'
    expected11 = True
    test('test11', s11, expected11)

    s12 = ' --6 '
    expected12 = False
    test('test12', s12, expected12)

    s13 = '.1'
    expected13 = True
    test('test13', s13, expected13)

    s14 = '-.1'
    expected14 = True
    test('test14', s14, expected14)

    s15 = '.'
    expected15 = False
    test('test15', s15, expected15)

    s16 = '6+1'
    expected16 = False
    test('test16', s16, expected16)

    s17 = '4e+'
    expected17 = False
    test('test17', s17, expected17)

    s18 = '.-4'
    expected18 = False
    test('test18', s18, expected18)

    s19 = ' -.'
    expected19 = False
    test('test19', s19, expected19)

    s20 = '96 e5'
    expected20 = False
    test('test20', s20, expected20)

    s21 = ' '
    expected21 = False
    test('test21', s21, expected21)

    s22 = '1 '
    expected22 = True
    test('test22', s22, expected22)

    s23 = 'ee'
    expected23 = False
    test('test23', s23, expected23)

    s24 = 'G76'
    expected24 = False
    test('test24', s24, expected24)
