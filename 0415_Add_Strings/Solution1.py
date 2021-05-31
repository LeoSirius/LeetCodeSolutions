class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        p1, p2 = len(num1)-1, len(num2)-1
        carry = 0
        while p1 >= 0 or p2 >= 0 or carry:
            v1, v2 = 0, 0
            if p1 >= 0:
                v1 = int(num1[p1])
                p1 -= 1
            if p2 >= 0:
                v2 =  int(num2[p2])
                p2 -= 1
            _sum = v1 + v2 + carry
            res.append(str(_sum % 10))
            carry = _sum // 10
        res.reverse()
        return ''.join(res)


def test(test_name, num1, num2, expected):
    res = Solution().addStrings(num1, num2)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    num11 = "11"
    num21 = "123"
    expected1 = "134"
    test('test1', num11, num21, expected1)

    num12 = '456'
    num22 = '77'
    expected2 = '533'
    test('test2', num12, num22, expected2)

    num13 = '0'
    num23 = '0'
    expected3 = '0'
    test('test3', num13, num23, expected3)
