class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            # odd case, 'aba'
            tmp = self.diffuse(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # even case, 'abba'
            tmp = self.diffuse(s, i, i + 1)
            if len(tmp) > len(res):
                res = tmp
        return res
            
    def diffuse(self, s: str, left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]