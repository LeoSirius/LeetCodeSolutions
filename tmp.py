class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            tmp = self.spread_out(s, i, i)  # case 'aba'
            if len(tmp) > len(res):
                res = tmp
            tmp = self.spread_out(s, i, i+1) # case 'abba'
            if len(tmp) > len(res):
                res = tmp
        return res

    def spread_out(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # 最后一次的left，right的索引已经不再符合条件，所以返回的时候不要包含它们
        return s[left+1:right]