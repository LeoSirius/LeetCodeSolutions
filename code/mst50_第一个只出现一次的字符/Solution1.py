from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> str:
        if not s:
            return ' '
        mp = defaultdict(int)
        for ch in s:
            mp[ch] += 1
        for k, v in mp.items():
            if v == 1:
                return k
        return ' '


def test(test_name, s, expected):
    res = Solution().firstUniqChar(s)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    s1 = 'abaccdeff'
    expected1 = 'b'
    test('test1', s1, expected1)

    s2 = ''
    expected2 = ' '
    test('test2', s2, expected2)


# 在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

# 示例:
# s = "abaccdeff"
# 返回 "b"

# s = "" 
# 返回 " "
#  

# 限制：
# 0 <= s 的长度 <= 50000
