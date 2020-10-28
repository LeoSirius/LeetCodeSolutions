
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        if n == 1:
            return 0
        return (m + self.lastRemaining(n-1, m)) % n


def test(test_name, n, m, expected):
    res = Solution().lastRemaining(n, m)
    if res == expected:
        print(f'{test_name} success.')
    else:
        print(f'{test_name} failed.')


if __name__ == "__main__":
    n1, m1, expected1 = 5, 3, 3
    test('test1', n1, m1, expected1)

    n2, m2, expected2 = 10, 17, 2
    test('test2', n2, m2, expected2)



# 0,1,,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。
# 求出这个圆圈里剩下的最后一个数字。

# 例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，
# 0, 1, 2, 3, 4
# 0, 1, 3, 4     -> 2
# 1, 3, 4        -> 0
# 1, 3           -> 4
# 3              -> 1
# 则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。

#  

# 示例 1：

# 输入: n = 5, m = 3
# 输出: 3
# 示例 2：

# 输入: n = 10, m = 17
# 输出: 2
#  

# 限制：

# 1 <= n <= 10^5
# 1 <= m <= 10^6
