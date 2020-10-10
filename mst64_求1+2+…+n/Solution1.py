class Solution:

    def __init__(self):
        self.res = 0

    def sumNums(self, n: int) -> int:

        def sum_nums(n):
            self.res += + n
            return n > 0 and int(sum_nums(n-1))

        sum_nums(n)
        return self.res

def test(test_name, n, expected):
    res = Solution().sumNums(n)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    n1, expected1 = 3, 6
    test('test1', n1, expected1)

    n2, expected2 = 9, 45
    test('test2', n2, expected2)



# 求 1+2+...+n ，
# 要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

# 示例 1：
# 输入: n = 3
# 输出: 6

# 示例 2：
# 输入: n = 9
# 输出: 45


# 限制：

# 1 <= n <= 10000