

class Solution:
    def __init__(self):
        self._dict = {}

    def isScramble(self, s1: str, s2: str) -> bool:
        if (s1, s2) in self._dict:
            return self._dict[(s1, s2)]

        l1, l2 = len(s1), len(s2)
        if l1 != l2 or sorted(s1) != sorted(s2):
            self._dict[(s1, s2)] = False
            return False

        if s1 == s2:
            self._dict[(s1, s2)] = True
            return True

        f = self.isScramble
        for i in range(1, l1):
            if f(s1[:i], s2[:i]) and f(s1[i:], s2[i:]) or\
               f(s1[:i], s2[-i:]) and f(s1[i:], s2[:-i]):
               self._dict[(s1, s2)] = True
               return True

        self._dict[(s1, s2)] = False
        return False

def test(test_name, s1, s2, expected):
    res = Solution().isScramble(s1, s2)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    s11, s21 = 'great', 'rgeat'
    expected1 = True
    test('test1', s11, s21, expected1)

    s12, s22 = 'abcde', 'caebd'
    expected2 = False
    test('test2', s21, s22, expected2)

    s13, s23 = 'a', 'a'
    expected3 = True
    test('test3', s13, s23, expected3)

    s14, s24 = 'abc', 'bca'
    expected4 = True
    test('test4', s14, s24, expected4)

    s15, s25 = 'eebaacbcbcadaaedceaaacadccd', 'eadcaacabaddaceacbceaabeccd'
    expected5 = False
    test('test5', s15, s25, expected5)

    s16, s26 = 'great', 'garte'
    expected6 = False
    test('test6', s16, s26, expected6)
