class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, max_len = 0, 0
        mapping = {}    # mapping char to it's index
        for i, char in enumerate(s):
            if char in mapping:
                # char is occured before, update start
                start = max(start, mapping[char] + 1)
            mapping[char] = i
            max_len = max(max_len, i - start + 1)   
        return max_len
