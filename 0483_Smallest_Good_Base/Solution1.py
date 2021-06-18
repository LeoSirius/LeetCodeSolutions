class Solution:
    def smallestGoodBase(self, n: str) -> str:
        
        num = int(n)
        # 给定 基数 和 位数长度，求对应全是1 的十进制的数
        def check(base, _len):
            res = 0
            for _ in range(_len+1):
                res = res * base + 1
            return res

        res = float('inf')

        # 遍历 m base 的数的长度
        for i in range(1, 64):
            l, r = 2, num
            # 这个 while 二分的是 base
            while l < r:
                mid = l + (r - l) // 2
                tmp = check(mid, i)
                if tmp == num:
                    res = min(res, mid)
                    break
                elif tmp > num:
                    r = mid
                else:
                    l = mid + 1
        return str(res)


def test(test_name, n, expected):
    res = Solution().smallestGoodBase(n)
    if type(res) == type(expected) and res == expected:
        print(test_name + ' succeed')
    else:
        print(test_name + ' failed')


if __name__ == '__main__':
    n1 = "13"
    expected1 = '3'
    test('test1', n1, expected1)

    n2 = '4681'
    expected2 = '8'
    test('test2', n2, expected2)

    n3 = '1000000000000000000'
    expected3 = '999999999999999999'
    test('test3', n3, expected3)
