class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ps, pt = 0, 0
        if not s:
            return True
        while pt < len(t) and ps < len(s):
            if s[ps] == t[pt]:
                ps += 1
                pt += 1
            else:
                pt += 1
        return ps == len(s)


def test(test_name, s, t, expected):
    res = Solution().isSubsequence(s, t)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    s1 = "abc"
    t1 = "ahbgdc"
    expected1 = True
    test('test1', s1, t1, expected1)

    s2 = "axc"
    t2 = "ahbgdc"
    expected2 = False
    test('test2', s2, t2, expected2)

    s3 = ""
    t3 = "ahbgdc"
    expected3 = True
    test('test3', s3, t3, expected3)

    s4 = 'b'
    t4 = 'abc'
    expected4 = True
    test('test4', s4, t4, expected4)

