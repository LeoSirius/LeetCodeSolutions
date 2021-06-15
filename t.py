
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = [0] * (max(len(a), len(b)) + 1)
        pa, pb, pc = len(a) - 1, len(b) - 1, len(res) - 1
        carry = 0

        while pa >= 0 or pb >= 0 or carry:
            v1, v2 = 0, 0
            if pa >= 0:
                v1 = int(a[pa])
                pa -= 1
            if pb >= 0:
                v2 = int(b[pb])
                pb -= 1
            _sum = v1 + v2 + carry
            res[pc] = _sum % 2
            pc -= 1
            carry = _sum // 2
        if res[0] == 0:
            res = res[1:]
        return ''.join([str(n) for n in res])




def test(test_name, a, b, expected):
    res = Solution().addBinary(a, b)
    # print(f'res = {res}')
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