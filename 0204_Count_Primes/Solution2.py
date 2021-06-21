class Solution:
    def countPrimes(self, n: int) -> int:
        # 先假定都是素数，后面再把不是素数的数筛掉

        is_prime = [True for i in range(n)]
        cnt = 0
        for i in range(2, n):
            if is_prime[i]:
                cnt += 1
            for j in range(i + i, n, i):
                is_prime[j] = False

        return cnt


def test(test_name, n, expected):
    res = Solution().countPrimes(n)
    if res == expected:
        print(test_name + ' succeed')
    else:
        print(test_name + ' fail')

if __name__ == "__main__":
    n1, expected1 = 10, 4
    test('test1', n1, expected1)
