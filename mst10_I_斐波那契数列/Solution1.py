class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        a, b = 0, 1
        for _ in range(n):
            a, b = b, (a + b) % 1000000007
        return a


def test(test_name, n, expected):
    res = Solution().fib(n)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    n1 = 2;  # 0 1
    expected1 = 1;
    test("test1", n1, expected1);

    n2 = 5;  # 0 1 1 2 3 5
    expected2 = 5;
    test("test1", n2, expected2);

    n3 = 45;
    expected3 = 134903163;
    test("test3", n3, expected3);


# 写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项。斐波那契数列的定义如下：

# F(0) = 0,   F(1) = 1
# F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
# 斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

# 答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

#  

# 示例 1：

# 输入：n = 2
# 输出：1
# 示例 2：

# 输入：n = 5
# 输出：5
#  

# 提示：

# 0 <= n <= 100
