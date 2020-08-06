class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for ch in s:
            if ch in ['(', '[', '{']:
                stk.append(ch)
            else:
                if not stk:
                    return False
                last = stk.pop()
                if ch == ')' and last != '(':
                    return False
                if ch == ']' and last != '[':
                    return False
                if ch == '}' and last != '{':
                    return False
        return stk == []


def test(test_name, s, expected):
    res = Solution().isValid(s)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    s1 = "()"
    expected1 = True
    test("test1", s1, expected1)

    s2 = "()[]{}"
    expected2 = True
    test("test2", s2, expected2)

    s3 = "(]"
    expected3 = False
    test("test3", s3, expected3)

    s4 = "([)]"
    expected4 = False
    test("test4", s4, expected4)

    s5 = "{[]}"
    expected5 = True
    test("test5", s5, expected5)

    s6 = "(])"
    expected6 = False
    test("test6", s6, expected6)
