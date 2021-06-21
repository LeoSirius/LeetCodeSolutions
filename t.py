class Solution:
    def countPrimes(self, n: int) -> int:
        isp = [True] * n
        res = 0

        for i in range(2, n):
            if isp[i]:
                res += 1
                j = i
                while j < n:
                    isp[j] = False
                    j += i

        return res


def test(test_name, n, expected):
    res = Solution().countPrimes(n)
    if res == expected:
        print(test_name + ' succeed')
    else:
        print(test_name + ' fail')

if __name__ == "__main__":
    n1, expected1 = 10, 4
    test('test1', n1, expected1)
