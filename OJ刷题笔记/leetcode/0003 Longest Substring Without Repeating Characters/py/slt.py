class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = maxLength = 0
        usedChar = {}
        
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)
            usedChar[s[i]] = i
            
        return maxLength

"""
start <= usedChar[s[i]]
这行代码的作用是把在start之前的在usedChar中的字符排除在外。
我们以‘tmmzuxta’为例。
当遇到第二个t时，start在第二个m的下标。如果不加这个判断，start会从t之后重新开始，最大长度是4。
但是我们的正确答案是6。
"""