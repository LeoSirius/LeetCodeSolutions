class Solution:
    def findNthDigit(self, n: int) -> int:
        n -= 1
        for digit in range(1, 12):
            first_num = pow(10, digit-1)

            if n < 9 * first_num * digit:
                return int(str(first_num + n // digit)[n % digit])
            n -= 9 * first_num * digit
        return 0


def test(test_name, n, expected):
    res = Solution().findNthDigit(n)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == "__main__":
    n1 = 3
    expected1 = 3
    test("test1", n1, expected1)

    n2 = 11
    expected2 = 0
    test("test2", n2, expected2)

    n3 = 365
    expected3 = 5
    test("test3", n3, expected3)

# 数字以0123456789101112131415…的格式序列化到一个字符序列中。
# 在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。

# 请写一个函数，求任意第n位对应的数字。

# 示例 1：
# 输入：n = 3
# 输出：3

# 示例 2：
# 输入：n = 11
# 输出：0

# 限制：
# 0 <= n < 2^31
