class Solution:
    def translateNum(self, num: int) -> int:
        if num <= 9:
            return 1

        res = num % 100       # res是最后两位
        if 10 <= res <= 25:
            return self.translateNum(num // 10) + self.translateNum(num // 100)
        else:
            return self.translateNum(num // 10)

def test(test_name, num, expected):
    res = Solution().translateNum(num)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == "__main__":
    num1 = 12258
    expected1 = 5
    test('test1', num1, expected1)


# 给定一个数字，我们按照如下规则把它翻译为字符串：
# 0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。
# 一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

# 示例 1:

# 输入: 12258
# 输出: 5

# 解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"

# 提示：
# 0 <= num < 2*31
