class Solution:
    def firstUniqChar(self, s: str) -> int:
        mp = {}
        for ch in s:
            if ch in mp:
                mp[ch] += 1
            else:
                mp[ch] = 1

        for i in range(len(s)):
            if mp[s[i]] == 1:
                return i

        return -1


def test(test_name, s, expected):
    res = Solution().firstUniqChar(s)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    s1 = 'leetcode'
    expected1 = 0
    test('test1', s1, expected1)

    s2 = 'loveleetcode'
    expected2 = 2
    test('test2', s2, expected2)


# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。


# 示例：

# s = "leetcode"
# 返回 0

# s = "loveleetcode"
# 返回 2

# 提示：你可以假定该字符串只包含小写字母。
