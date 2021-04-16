

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        pass



def test(test_name, s1, s2, expected):
    res = Solution().isScramble(s1, s2)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    # s11, s21 = 'great', 'rgeat'
    # expected1 = True
    # test('test1', s11, s21, expected1)

    # s12, s22 = 'abcde', 'caebd'
    # expected2 = False
    # test('test2', s21, s22, expected2)

    # s13, s23 = 'a', 'a'
    # expected3 = True
    # test('test3', s13, s23, expected3)

    # s14, s24 = 'abc', 'bca'
    # expected4 = True
    # test('test4', s14, s24, expected4)

    s15, s25 = 'eebaacbcbcadaaedceaaacadccd', 'eadcaacabaddaceacbceaabeccd'
    expected5 = True
    test('test5', s15, s25, expected5)
