class Solution:
    def addBinary(self, a: str, b: str) -> str:
        p1, p2 = len(a) - 1, len(b) - 1
        res_int_list = []
        carry = 0
        while p1 >= 0 or p2 >= 0 or carry:
            v1, v2 = 0, 0
            if p1 >= 0:
                v1 = int(a[p1])
                p1 -= 1
            if p2 >= 0:
                v2 = int(b[p2])
                p2 -= 1

            cur_sum = carry + v1 + v2
            res_int_list.insert(0, cur_sum % 2)
            carry = cur_sum // 2

        return ''.join([str(num) for num in res_int_list])


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
