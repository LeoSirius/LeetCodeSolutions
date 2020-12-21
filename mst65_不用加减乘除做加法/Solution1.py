class Solution:
    def add(self, a: int, b: int) -> int:
        carry = 0
        x = 0xffffffff
        a, b = a & x, b & x   # 从无限长度变为一个 32 位整数的补码
        # 如-1补码是0b11111111111111111111111111111111
        # 这样就可以像其他语言一样运算了
        while b != 0:
            a, b = (a ^ b), (a & b) << 1 & x

        # 0x7fffffff 是最大的正数的补码
        # 如果a没有超过这个数，则直接返回
        # 如果超过，说明是负数，
        # a ^ x 运算将 1 至 32 位按位取反， ~ 运算是将整个数字取反
        # ~(a ^ x) 是将 32 位以上的位取反，1 至 32 位不变。
        return a if a <= 0x7fffffff else ~(a ^ x)


def test(test_name, a, b, expected):
    res = Solution().add(a, b)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":

    a1, b1 = 1, 1
    expected1 = 2
    test('test1', a1, b1, expected1)

    a2, b2 = -1, 2
    expected2 = 1
    test('test2', a2, b2, expected2)


# 写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。


# 示例:

# 输入: a = 1, b = 1
# 输出: 2
#  

# 提示：

# a, b 均可能是负数或 0
# 结果不会溢出 32 位整数
