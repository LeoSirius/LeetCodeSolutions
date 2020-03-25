class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fac = [1]   # 阶乘的list，fac[i] = i!
        for i in range(1, n + 1):
            fac.append(i * fac[i-1])

        num_char = ''.join([str(i+1) for i in range(n)])  # num_char 存放字符，如n=4，则num_char = '1234'

        res = ''
        k -= 1
        for i in range(n-1, -1, -1):
            idx = k // fac[i]
            k -= fac[i] * idx

            res += num_char[idx]
            num_char = num_char[:idx] + num_char[idx+1:]

        return res


def test(test_name, n, k, expected):
    res = Solution().getPermutation(n, k)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == "__main__":
    n1, k1, expected1 = 3, 3, "213"
    test('test1', n1, k1, expected1)

    n2, k2, expected2 = 4, 9, "2314"
    test('test2', n2, k2, expected2)
