class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # [l, r] 左右都闭
        l, r = 0, 0
        history_char_max = 0
        ch_map = [0] * 26               # 保存当前窗口内各个字符出现的次数

        while r < len(s):
            idx = ord(s[r]) - ord('A')
            ch_map[idx] += 1
            history_char_max = max(history_char_max, ch_map[idx])

            if r - l + 1 > history_char_max + k:
                ch_map[ord(s[l])-ord('A')] -= 1
                l += 1

            r += 1

        return len(s) - l


def test(test_name, s, k, expected):
    res = Solution().characterReplacement(s, k)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    s1 = 'ABAB'
    k1 = 2
    expected1 = 4
    test('test1', s1, k1, expected1)

    s2 = 'AABABBA'
    k2 = 1
    expected2 = 4
    test('test2', s2, k2, expected2)


# Given a string s that consists of only uppercase English letters,
#  you can perform at most k operations on that string.

# In one operation, you can choose any character of the string
#  and change it to any other uppercase English character.

# Find the length of the longest sub-string containing all 
# repeating letters you can get after performing the above operations.

# Note:
# Both the string's length and k will not exceed 104.

# Example 1:

# Input:
# s = "ABAB", k = 2

# Output:
# 4

# Explanation:
# Replace the two 'A's with two 'B's or vice versa.
#  
# Example 2:

# Input:
# s = "AABABBA", k = 1

# Output:
# 4

# Explanation:
# Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.

