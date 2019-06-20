## 思路1 用一个dict存放出现过的character

使用usedChar存放出现过的字符，key是那个字符，value是字符对应的索引。

`start <= usedChar[s[i]]`
这行代码的作用是把在start之前的在usedChar中的字符排除在外。

我们以‘tmmzuxta’为例。当遇到第二个t时，start在第二个m的下标。如果不加这个判断，start会从t之后重新开始，最大长度是4。但是我们的正确答案是6。


```py
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
```