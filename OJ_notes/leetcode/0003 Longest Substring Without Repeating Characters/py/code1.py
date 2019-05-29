class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used_char = {}
        max_len = start = 0
        for i, char in enumerate(s):
            if char in used_char and start <= used_char[char]:
                start = used_char[char] + 1
            else:
                max_len = max(max_len, i - start + 1)
            used_char[char] = i
        return max_len