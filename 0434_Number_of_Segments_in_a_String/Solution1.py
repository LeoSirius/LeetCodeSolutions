class Solution:
    def countSegments(self, s: str) -> int:
        res = 0
        if not s:
            return res

        l, r = 0, len(s) - 1
        while l < len(s) and s[l] == ' ':
            l += 1
        while r >= 0 and s[r] == ' ':
            r -= 1
        if l > r:
            return res

        in_word = s[l] != ' '
        for i in range(l, r+1):
            if s[i] != ' ':
                in_word = True
            else:
                if in_word:
                    in_word = False
                    res += 1

        return res + 1


def test(test_name, s, expected):
    res = Solution().countSegments(s)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    s1 = 'Hello, my name is John'
    expected1 = 5
    test('test1', s1, expected1)

    s2 = 'Hello'
    expected2 = 1
    test('test2', s2, expected2)

    s3 = "love live! mu'sic foreve'"
    expected3 = 4
    test('test3', s3, expected3)

    s4 = ''
    expected4 = 0
    test('test4', s4, expected4)

    s5 = '       '
    expected5 = 0
    test('test5', s5, expected5)

    s6 = 'a'
    expected6 = 1
    test('test6', s6, expected6)

    s7 = '   foo bar'
    expected7 = 2
    test('test7', s7, expected7)
