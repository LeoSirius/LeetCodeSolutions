from collections import deque

class Solution:
    def reverseParentheses(self, s: str) -> str:
        if not s:
            return ''

        dq = deque()     # 用 list 比用 arr 快
        for ch in s:
            if ch != ')':
                dq.append(ch)
            else:
                _str = ''
                while dq[-1] != '(':
                    _str += dq.pop()
                dq.pop()
                for c in _str:
                    dq.append(c)


def test(test_name, s, expected):
    res = Solution().reverseParentheses(s)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    s1 = "(abcd)"
    expected1 = "dcba"
    test('test1', s1, expected1)

    s2 = "(u(love)i)"
    expected2 = "iloveu"
    test('test2', s2, expected2)

    s3 = "(ed(et(oc))el)"
    expected3 = 'leetcode'
    test('test3', s3, expected3)

    s4 = "a(bcdefghijkl(mno)p)q"
    expected4 = 'apmnolkjihgfedcbq'
    test('test4', s4, expected4)
