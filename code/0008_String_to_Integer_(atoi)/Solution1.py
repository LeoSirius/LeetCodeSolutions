class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip(' ')
        if not s:
            return 0

        sign = 1
        if s[0] in ['-', '+']:
            if s[0] == '-':
                sign = -1
            s = s[1:]

        p, res = 0, 0
        while p < len(s) and s[p].isnumeric():
            res = res * 10 + int(s[p])
            p += 1

        return max(-(2**31), min(2**31-1, sign * res))

def test(test_name, s, expected):
    res = Solution().myAtoi(s)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == "__main__":
    test('test1', '42', 42)
    test('test2', '   -42', -42)
    test('test3', '4193 with words', 4193)
    test('test4', 'words and 987', 0)
    test('test5', '-91283472332', -2147483648)
    test('test6', '3.14159', 3)
    test('test7', '', 0)
