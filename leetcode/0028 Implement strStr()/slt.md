## 思路1 用python的切片

题目是叫我们实现这个函数，而不是调用这个函数。

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1 
```