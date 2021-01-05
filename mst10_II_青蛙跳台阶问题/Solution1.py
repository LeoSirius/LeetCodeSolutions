class Solution:
    def numWays(self, n: int) -> int:
        if n <= 1:
            return 1

        last1, last2 = 1, 1
        for _ in range(2, n + 1):
            tmp = (last1 + last2) % 1000000007
            last2 = last1
            last1 = tmp

        return last1


def test(test_name, n, expected):
    res = Solution().numWays(n)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    n1 = 2;
    expected1 = 2;
    test("test1", n1, expected1);

    n2 = 7;
    expected2 = 21;
    test("test2", n2, expected2);

    n3 = 0;
    expected3 = 1;
    test("test3", n3, expected3);


# 一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

# 答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

# 示例 1：

# 输入：n = 2
# 输出：2
# 示例 2：

# 输入：n = 7
# 输出：21
# 示例 3：

# 输入：n = 0
# 输出：1
# 提示：

# 0 <= n <= 100