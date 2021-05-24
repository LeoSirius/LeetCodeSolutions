class Solution:
    def addBinary(self, a: str, b: str) -> str:
        p1, p2 = len(a)-1, len(b)-1
        carry = 0
        res = ['0'] * (max(len(a), len(b)) + 1)
        p3 = len(res)-1

        while carry or p1 >= 0 or p2 >= 0:
            v1, v2 = 0, 0
            if p1 >= 0:
                v1 = a[p1]
                p1 -= 1
            if p2 >= 0:
                v2 = b[p2]
                p2 -= 1
            _sum = carry + int(v1) + int(v2)
            carry = _sum // 2
            cur = _sum % 2
            res[p3] = str(cur)
            p3 -= 1

        return ''.join(res[p3+1:])


def test(test_name, a, b, expected):
    res = Solution().addBinary(a, b)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    a1, b1 = '11', '1'
    expected1 = '100'
    test("test1", a1, b1, expected1)

    a2, b2 = '1010', '1011'
    expected2 = '10101'
    test('test2', a2, b2, expected2)
