class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, max_len = 0, 0
        my_dict = {}
        for i, char in enumerate(s):
            if char in my_dict:
                start = max(start, my_dict[char]+1)
            my_dict[char] = i
            max_len = max(max_len, i-start+1)
        return max_len