class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ch2idx = {}
        start, max_len = 0, 0
        for i in range(len(s)):
            if s[i] in ch2idx.keys():
                # 是之前那个已经出现的过字符的索引，如abca，ch2idx[s[i]]就是第一个a的索引
                start = max(start, ch2idx[s[i]] + 1)
            ch2idx[s[i]] = i
            max_len = max(max_len, i - start + 1)
        return max_len


def test(test_name, s, expected):
    res = Solution().lengthOfLongestSubstring(s)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == "__main__":
    s1, expected1 = "abcabcbb", 3
    test('test1', s1, expected1)

    s2, expected2 = " ", 1
    test('test2', s2, expected2)
