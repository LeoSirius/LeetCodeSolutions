from collections import Counter

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        for i in range(len(s)):
            if s.find(s[i]) != t.find(t[i]):
                return False
        return True


def test(test_name, s, t, expected):
    res = Solution().isIsomorphic(s, t)
    if type(res) == type(expected) and res == expected:
        print(test_name + ' succeed')
    else:
        print(test_name + ' fail')


if __name__ == '__main__':
    s1 = "egg"
    t1 = "add"
    expected1 = True
    test('test1', s1, t1, expected1)

    s2 = "foo"
    t2 = "bar"
    expected2 = False
    test('test2', s2, t2, expected2)

    s3 = "paper"
    t3 = "title"
    expected3 = True
    test('test3', s3, t3, expected3)
