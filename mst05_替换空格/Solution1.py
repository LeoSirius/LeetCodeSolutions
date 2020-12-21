class Solution:
    def replaceSpace(self, s: str) -> str:
        space_cnt = 0
        for ch in s:
            if ch == ' ':
                space_cnt += 1
        
        res = [' '] * (space_cnt * 2 + len(s))
        p = len(res)-1
        for i in range(len(s)-1, -1, -1):
            if s[i] == ' ':
                res[p] = '0'
                p -= 1
                res[p] = '2'
                p -= 1
                res[p] = '%'
                p -= 1
            else:
                res[p] = s[i]
                p -= 1

        return ''.join(res)


def test(test_name, s, expected):
    res = Solution().replaceSpace(s)
    if res == expected:
        print(f'{test_name} success.')
    else:
        print(f'{test_name} failed.')


if __name__ == "__main__":
    s1 = "We are happy."
    expected1 = "We%20are%20happy."
    test('test1', s1, expected1)


# 请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

# 示例 1：

# 输入：s = "We are happy."
# 输出："We%20are%20happy."
#  

# 限制：

# 0 <= s 的长度 <= 10000

