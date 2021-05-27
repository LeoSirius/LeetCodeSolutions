class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        xor_bit_cnt = 0

        for i in range(31):
            bit = (xor >> i) & 1
            xor_bit_cnt += bit
        return xor_bit_cnt


def test(test_name, x, y, expected):
    res = Solution().hammingDistance(x, y)
    print(f'res = {res}')
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == '__main__':
    x1 = 1
    y1 = 4
    expected1 = 2
    test('test1', x1, y1, expected1)

    x2 = 3
    y2 = 1
    expected2 = 1
    test('test2', x2, y2, expected2)
