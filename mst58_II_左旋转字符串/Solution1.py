class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[:n]


def test(test_name, s, n, expected):
    res = Solution().reverseLeftWords(s, n)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    s1 = "abcdefg"
    k1 = 2
    expected1 = "cdefgab"
    test('test1', s1, k1, expected1)

    s2 = "lrloseumgh"
    k2 = 6
    expected2 = "umghlrlose"
    test('test2', s2, k2, expected2)


# 字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。
# 请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，
# 该函数将返回左旋转两位得到的结果"cdefgab"。

# 示例 1：

# 输入: s = "abcdefg", k = 2
# 输出: "cdefgab"

# 示例 2：

# 输入: s = "lrloseumgh", k = 6
# 输出: "umghlrlose"
#  

# 限制：

# 1 <= k < s.length <= 10000

